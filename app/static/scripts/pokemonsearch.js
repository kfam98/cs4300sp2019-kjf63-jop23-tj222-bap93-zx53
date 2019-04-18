var dataList = []; // for dataset

//for passing arugments
var curr_pokemon_moveset;
var l_bool = false;
var generations;
var pstyle;
var caprate = '.1';
var myteam;
var giveOppTeam = false;
var theirteam;



$.getJSON("/static/data/pokemondata.json", function(json) {
  for (var i = 0; i < json.length; i++) {
    dataList.push({id: json[i].pokedex_number, text: json[i].name});
  }

  function formatState(state) {
    if (!state.id) {
      return state.text;
    }
    var $state = $(
      '<span><img src="' + json[state.id-1].imgSrc + '" class="select-img" /> <span class="select-text">' + state.text + '</span></span>'
    );
    return $state;
  };

  function formatCard(pokedexNumber) {
    var imgSrc = "";
    var name = ""
    for (var i = 0; i < json.length; i++) {
      if (json[i].pokedex_number == pokedexNumber) {
        imgSrc = json[i].imgSrc;
        name = json[i].name;
        curr_pokemon_moveset = json[i].moveset;
      }
    }
    var $card = $(
      '<div class="pokemon-card-form"><img class="pokemon-card-img" alt="pokemon" src="' + imgSrc + '"><div class="pokemon-card-name">' + name + '</div><div class="pokemon-nature-label"></div><div class="pokemon-moveset-label"></div><div class="remove-pokemon-button">&times;</div></div>'
    );
    // var $natureSelect = $(
    //   "<span class='nature-select2'><input type='text' placeholder='nature' name='nature' style='width:100px' /></span>"
    // );
    // $card.append($natureSelect);
    // initializeNatureSelect2($natureSelect);
    var $movesetSelect = $(
      "<span class='moveset-select2'><input type='text' placeholder='moveset' name='moveset' style='  overflow-y: scroll; width:250px' /></span>"
    );
    $card.append($movesetSelect);
    initializeMovesetSelect2($movesetSelect);


    return $card
  }

  // init select 2
  function initializeSelect2(obj) {
    obj.select2({
      data: dataList,

      formatResult: formatState,
      formatSelection: formatState,
      escapeMarkup: function(m) { return m; },

      initSelection: function(element, callback) {
          callback({ id: element.val(), text: element.attr('data-init-text') });
      },

      // NOT NEEDED: text for loading more results
      formatLoadMore: function() {return 'Loading more...'},

      // query with pagination
      query: function (q) {
        var pageSize,
          results;
        pageSize = 20; // or whatever pagesize
        var results  = [];
        if (q.term && q.term !== "") {
          // HEADS UP; for the _.filter function i use underscore (actually lo-dash) here
          var results = this.data;
          var results = _.filter(results, function (e) {
            if(typeof e.children != 'undefined')
            {
              subresults = _.filter(e.children, function (f) {
                return (f.text.toUpperCase().indexOf(q.term.toUpperCase()) >= 0);
              });
              if(subresults.length > 0)
                return true;
              return false;
            }
            return (e.text.toUpperCase().indexOf(q.term.toUpperCase()) >= 0);
          });
          newresults = [];
          for (var i = 0, len = results.length; i < len; i++) {
          newresults[i] = {};
          if(typeof results[i].text != 'undefined')
            newresults[i].text = results[i].text;
          if(typeof results[i].id != 'undefined')
            newresults[i].id = results[i].id;
          if(typeof results[i].children != 'undefined')
          {
            newresults[i].children = results[i].children;
            newresults[i].children = _.filter(newresults[i].children, function (f) 							{
                return (f.text.toUpperCase().indexOf(q.term.toUpperCase()) >= 0);
              });
          }
        }
        results = newresults;
        } else if (q.term == "") {
          results = this.data;

        }

        q.callback({
          results: results.slice((q.page - 1) * pageSize, q.page * pageSize),
          more   : results.length >= q.page * pageSize
        });
      }
    });
  }


  $(".add-pokemon-button").on("click", function() {
    var newSelect = $("<span class='pokemon-select2'><input type='text' name='pokemon' style='width:250px' /></span>");
    $(this).parent().append(newSelect);
    initializeSelect2(newSelect);
    $(this).hide();
  });


  //removing a pokemon
  $(document).on("click", ".remove-pokemon-button", function() {
    $(this).parent().parent().children('.add-pokemon-button').show();
    $(this).parent().attr('id', 'remove-card');
    $('#remove-card').remove();

  });


  //selecting a pokemon --> formats pokemon card
  $(document).on("change", ".pokemon-select2", function() {
    console.log($(this).val());
    // console.log($.trim($(this).text()));
    // $(this).parent().append(formatCard($.trim($(this).text())));
    $(this).parent().append(formatCard($(this).val()));
    $(this).parent().children('.pokemon-select2').hide();
      // var $this = $(this);
      // $("#here").addClass('loading');
      // $("#here").empty();
      // // alert($this.val());
      // $.getJSON($SCRIPT_ROOT + '/update_selected_location', {
      //   id: $this.val()
      // }, function(data) {
      //   $("#here").html(data.result);
      //   $("#here").removeClass('loading');
      // });
      // return false;
  });

});

//////////////////////////////
// initializers for filters//
//////////////////////////////
function initializeNatureSelect2(obj) {
  obj.select2({
    data: naturesLst,
  });
}

function initializeMovesetSelect2(obj) {

  var moveset = [];
  var i = 1;
  curr_pokemon_moveset.forEach( function(move) {
    moveset.push({'id': i, 'text': move});
    i++;
  });
  obj.select2({
    data: moveset,
    multiple: "multiple",
    maximumSelectionSize: 4
  });
}

function initializeFilterGenerationSelect2(obj) {
  obj.select2({
    data: genLst,
    multiple: "multiple",
  });
}

function initializeFilterLeagueSelect2(obj) {
  obj.select2({
    data: leaguesLst,
    // multiple: "multiple",
  });
}

function initializeFilterPlaystyleSelect2(obj) {
  obj.select2({
    data: pstyleLst,
  });
}


// var initialSelect = $("<span class='pokemon-select2'><input type='text' name='pokemon' style='width:250px' /></span>");
// initializeSelect2(initialSelect);
// $('#initial-select-container').append(initialSelect);

$(".nature-select2").each(function() {
  initializeNatureSelect2($(this));
});

$(".moveset-select2").each(function() {
  initializeMovesetSelect2($(this));
});

$(".filter-generation-select2").each(function() {
  initializeFilterGenerationSelect2($(this));
});

$(".filter-playstyle-select2").each(function() {
  initializeFilterPlaystyleSelect2($(this));
});

$(".filter-leagues-select2").each(function() {
  initializeFilterLeagueSelect2($(this));
});



////////////////////
//filters setting///
////////////////////
$(".opponent-team-container").hide();
$(".opponent-team-header").hide();
$("#yes").css('background-color', '#282429');

$("#yes").on("click", function() {

    $(".opponent-team-container").show();
    $(".opponent-team-header").show();
    $("#yes").css('background-color', '#fc0d1b');
    $("#no").css('background-color', '#282429');
    giveOppTeam = true;

  });

$("#no").on("click", function() {

  $(".opponent-team-container").hide();
  $(".opponent-team-header").hide();
  $("#no").css('background-color', '#fc0d1b');
  $("#yes").css('background-color', '#282429');
  giveOppTeam = false;

});

$("#yes_legend").css('background-color', '#282429');

$("#yes_legend").on("click", function() {

  $("#yes_legend").css('background-color', '#fc0d1b');
  $("#no_legend").css('background-color', '#282429');
  l_bool = true;

});

$("#no_legend").on("click", function() {
$("#no_legend").css('background-color', '#fc0d1b');
$("#yes_legend").css('background-color', '#282429');
l_bool = false;

});

$(document).on('input', "#myRange", function() {
$('#capture-rate').html( $(this).val() + "%");
caprate = '' + $(this).val();
});


//CREATE THE GENERATION LINK
//CHECK IF ANY REQUIRED THINGS R NULL!!!!!
$(document).on("click", ".generate-recommendations-button", function() {
  pstyle = $('#select2-chosen-4').html();
  league = $('#select2-chosen-6').html();

  var gens_str= '';
  $(".select2-search-choice > div").each(function() {
  gens_str+=(romanToNumbers[this.innerHTML])+"+";
  });

  generations = gens_str;

  var myteam_str='';
  $(".your-team-container > .team-slot-container >.pokemon-card-form").each(function() {
  li_lst = this.children[5].children;
  mv = '';
  for (var i = 0; i < li_lst.length; i++) {
    var li = li_lst[i];
    if (li.className == "select2-choices") {
      mv += li.innerText.replace(/(\r\n|\n|\r)/gm, '6');

    }
  }
  myteam_str += this.children[1].innerText + "6" + mv+"_";
  });
  //console.log(myteam_str);
  var theirteam_str='';
  var results_url;
  if (giveOppTeam) {

  $(".opponent-team-container > .team-slot-container >.pokemon-card-form").each(function() {
    li_lst = this.children[5].children;
    mv = '';
    for (var i = 0; i < li_lst.length; i++) {
      var li = li_lst[i];
      if (li.className == "select2-choices") {
        mv += li.innerText.replace(/(\r\n|\n|\r)/gm, '6');

      }
    }
    theirteam_str += this.children[1].innerText + "6" + mv+"_";
  });



  //console.log(theirteam_str);
  results_url = '/results?legendary='+l_bool+"&league="+league+"&gens="+generations+"&pstyle="+pstyle+"&caprate="+caprate+"&myteam="+myteam_str+"&theirteam="+theirteam_str;

  } else {
  results_url = '/results?legendary='+l_bool+"&league="+league+"&gens="+generations+"&pstyle="+pstyle+"&caprate="+caprate+"&myteam="+myteam_str;
  }
  // console.log(generations);
  // console.log(caprate);


  ///////////////////////////////////
  ///check if all inputs were enter//
  //////////////////////////////////
  if (generations == '') {
  $('#generation-error').html("Please enter a generation(s)");
  $('#generation-error').css("display", "block");
  } else {
  $('#generation-error').html("");
  $('#generation-error').css("display", "none");
  }

  if (league == '&nbsp;') {
  $('#leagues-error').html("Please choose a league");
  $('#leagues-error').css("display", "block");
  } else {
  $('#leagues-error').html("");
  $('#leagues-error').css("display", "none");
  }

  if (pstyle == '&nbsp;')  {
  $('#playstyle-error').html("Please choose a playstyle");
  $('#playstyle-error').css("display", "block");
  } else {
  $('#playstyle-error').html("");
  $('#playstyle-error').css("display", "none");
  }

  if ((generations != '') && (league != '&nbsp;') && (pstyle != '&nbsp;')) {
  window.location.href = results_url;
  } else {
  alert("Missing fields. Check your filters!");
  }

});

$('.site-icon').hover( function() {
  $('.site-icon').attr('src', '/static/images/icon4.png');
});

$('.site-icon').mouseout( function() {
  $('.site-icon').attr('src', '/static/images/icon3.png');
});