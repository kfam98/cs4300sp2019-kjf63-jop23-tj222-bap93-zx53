var dataList = []; // for dataset

//for passing arugments
var curr_pokemon_moveset;
var l_bool = false;
var generations;
var pstyle;
var caprate = '10';
var myteam;
var giveOppTeam = false;
var theirteam;

//for keeping filters
var selectedGenerations = ['1','2','3','4','5','6','7'];
var selectedLegendary = 0;


$.JSON("/static/data/pokemondata3.json", function(json) {
  for (var i = 0; i < json.length; i++) {
    dataList.push({id: i, text: json[i].name, generation: json[i].generation, legendary: json[i].legendary});
  }

  function formatState(state) {
    if (!json[state.id].pokedex_number) {
      return state.text;
    }
    var $state = $(
      '<span><img src="' + json[state.id].imgSrc + '" class="select-img" /> <span class="select-text">' + state.text + '</span></span>'
    );
    return $state;
  };

  function formatCard(i) {
    // var imgSrc = "";
    // var name = "";
    // var type1='';
    // var type2='';
    // for (var i = 0; i < json.length; i++) {
      // if (json[i].pokedex_number == pokedexNumber) {
    imgSrc = json[i].imgSrc;
    name = json[i].name;
    curr_pokemon_moveset = json[i].moveset;
    type1 = json[i].type1;
    type2 = json[i].type2;


    if (type2 == null) {
      type2 = '';
    }

      // }
    // }


    var $card = $(
      '<div class="pokemon-card-form"><img class="pokemon-card-img" alt="pokemon" src="' + imgSrc + '"><div class="pokemon-card-name"><span class="name">' + name + '</div><div class="pokemon-card-type"></span><span class="type" style="background-color: ' + types[type1] + ';" >' + type1 + '</span><span class="type" style="background-color: ' + types[type2] + ';">' + type2 + '</span></div><div class="pokemon-nature-label"></div><div class="pokemon-moveset-label"></div><div class="remove-pokemon-button">&times;</div></div>'
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

function getDataList() {
  console.log(selectedGenerations);
  var filtered =  dataList.filter(function(pokemon){
                    // console.log(pokemon.generation);
                    return (selectedGenerations.includes(""+pokemon.generation) && (pokemon.legendary <= selectedLegendary));
                    // return pokemon.generation == 2;
                  });

  var newDataList = filtered.map((pokemon) => {
    return {
      id: pokemon.id,
      text: pokemon.text
    }
  })
  // console.log(newDataList);
  return newDataList
  // console.log(filtered);
}

  // init select 2
  function initializeSelect2(obj) {
    obj.select2({
      data: getDataList(),
      placeholder: "Select a Pokemon",
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
      $(this).parent().children('.pokemon-select2').remove();
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


    $(document).ready(function() {
      var newSelect = $("<span class='pokemon-select2'><input type='text' name='pokemon' style='width:250px' /></span>");
      $("#initial-select-container").append(newSelect);
      initializeSelect2(newSelect);
      $("#initial-select-container").children('.add-pokemon-button').hide();
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
      placeholder: "Moveset (optional)",
      multiple: "multiple",
      maximumSelectionSize: 4,
      allowClear: true
    });
    $('.select2-search__field').css('width', '100%');
  }

  function initializeFilterGenerationSelect2(obj) {
    obj.select2({
      data: genLst,
      multiple: "multiple",
    }).select2('val', [1,2,3,4,5,6,7]);
  }

  function initializeFilterLeagueSelect2(obj) {
    obj.select2({
      data: leaguesLst,
      // multiple: "multiple",
    }).select2('val', '1');

  }

  function initializeFilterPlaystyleSelect2(obj) {
    obj.select2({
      data: pstyleLst,
    }).select2('val', '2');
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


  $(".filter-generation-select2").on("change", function (e) {
    console.log($(".filter-generation-select2").select2("val"));
    selectedGenerations = $(".filter-generation-select2").select2("val");
    $('.pokemon-select2').siblings('.add-pokemon-button').show();
    $('.pokemon-select2').remove();
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
    if (l_bool != true) {
      $('.pokemon-select2').siblings('.add-pokemon-button').show();
      $('.pokemon-select2').remove();
    }
    l_bool = true;
    selectedLegendary = 1;

  });

  $("#no_legend").on("click", function() {
    $("#no_legend").css('background-color', '#fc0d1b');
    $("#yes_legend").css('background-color', '#282429');
    if (l_bool != false) {
      $('.pokemon-select2').siblings('.add-pokemon-button').show();
      $('.pokemon-select2').remove();
    }
    l_bool = false;
    selectedLegendary = 0;
  });

  $(document).on('input', "#myRange", function() {
  $('#capture-rate').html( $(this).val() + "%");
  caprate = '' + $(this).val();
  console.log("caprate: " + caprate);
  });


  //CREATE THE GENERATION LINK
  //CHECK IF ANY REQUIRED THINGS R NULL!!!!!
  $(document).on("click", ".generate-recommendations-button", function() {
    pstyle = $('#select2-chosen-4').html();
    if (pstyle == "Offensive") {
      psytle = "Glass-Cannon";
    }
    league = $('#select2-chosen-6').html();

    var gens_str= '';
    $(".select2-search-choice > div").each(function() {
    gens_str+=(romanToNumbers[this.innerHTML])+"+";
    });

    generations = gens_str;

    var myteam_str='';
    $(".your-team-container > .team-slot-container >.pokemon-card-form").each(function() {
    li_lst = this.children[6].children[0].children;
    // console.log(li_lst);
    mv = '';
    for (var i = 0; i < li_lst.length; i++) {
      var li = li_lst[i];
      if (li.className == "select2-search-choice") {
        console.log(li.innerText);
        mv += li.innerText.replace(/(\r\n|\n|\r)/gm, '');
        mv+='6';


      }
    }
    myteam_str += this.children[1].innerText + "6" + mv+"_";

    });
    //console.log(myteam_str);
    var theirteam_str='';
    var results_url;
    if (giveOppTeam) {

    $(".opponent-team-container > .team-slot-container >.pokemon-card-form").each(function() {
      li_lst = this.children[6].children[0].children;

      mv = '';
      for (var i = 0; i < li_lst.length; i++) {
        var li = li_lst[i];
        if (li.className == "select2-sesarch-choice") {
          mv += li.innerText.replace(/(\r\n|\n|\r)/gm, '');
          mv+='6';

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

});
