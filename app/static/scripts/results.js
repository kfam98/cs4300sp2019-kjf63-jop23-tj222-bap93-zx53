
  //use to print stats about each pokemon
  $.getJSON("/static/data/pokemon_stats.json", function(json) {

    $('.ptooltip').hover( function() {


      var name = $(this).parent().children()[1].innerText;

      var stats = json[name];
      var nature = $($(this).parent().children()[3]).children()[0].innerHTML.split(" ")[0].slice(0, -1);



      var hp = stats['hp'];
      var speed = stats['speed'];
      var defense = stats['defense'];
      var attack = stats['attack'];
      var sp_attack = stats['sp_attack'];
      var sp_defense = stats['sp_defense'];

      var nature_mapping = {
        'hp': hp,
        'speed': speed,
        'attack': attack,
        'defense':defense,
        'special attack': sp_attack,
        'special defense': sp_defense,
      }

      if (nature != "None") {
        if (nature.split('/').length == 2) {
          nature = nature.split('/');
          for (var i = 0; i < 2; i++) {
            var increased = natureStats[nature[i]]['increase'];
            var decreased = natureStats[nature[i]]['decrease'];

            nature_mapping[increased] = nature_mapping[increased] + (nature_mapping[increased] * .10);
            nature_mapping[decreased] = nature_mapping[decreased] - (nature_mapping[decreased] * .10);

          }
        } else {

          var increased = natureStats[nature]['increase'].toLowerCase();
          var decreased = natureStats[nature]['increase'].toLowerCase();

          nature_mapping[increased] = nature_mapping[increased] + (nature_mapping[increased] * .10);
          nature_mapping[decreased] = nature_mapping[decreased] - (nature_mapping[decreased] * .10);
        }
      }


      var stats_scale = d3.scaleLinear()
      .domain([0, 230])
      .range([0,150]);
      var str = '<span style="font-size:16px;">STATISTICS<br/> </span><span class="stats-name">HP: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(hp)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(hp))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ hp +'</div><br/>' ;
      str += '<span class="stats-name">ATTACK: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(attack)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(attack))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ attack +'</div><br/>' ;
      str += '<span class="stats-name">DEFENSE: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(defense)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(defense))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ defense +'</div><br/>' ;
      str += '<span class="stats-name">SPEED: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(speed)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(speed))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ speed +'</div><br/>' ;
      str += '<span class="stats-name">SP ATTACK: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(sp_attack)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(sp_attack))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ sp_attack +'</div><br/>' ;
      str += '<span class="stats-name">SP DEFENSE: </span><div class="stats-bar"> <div style="float:left;height:10px;background-color:#7AC74C;width:' + Math.round(stats_scale(sp_defense)) + 'px";></div><div class="stats-bar" style="float:left;height:10px;background-color:#d8d8d8;width:' + (150 - Math.round(stats_scale(sp_defense))) + 'px";></div><span class="stats-name" style="padding-left:3%;">  '+ sp_defense+'</div>' ;

      $($(this).children()[0]).html(str);
      $($($(this).parent().children()[0]).children()[1]).html(str);

    });

  });


  //looking between teams
  var curr_team = 1;
  for (var i=2; i < 6; i++) {
    $("#team-"+i).hide();
    $("#team-title-"+i).hide();
  }

  $("#left").on("click", function() {
    $("#team-"+curr_team).hide();
    $("#team-title-"+curr_team).hide();

    var new_team = curr_team - 1;
    if (new_team == 0) {
      new_team = 5;

    }
    curr_team = new_team;


    $("#team-"+new_team).show();
    $("#team-title-"+new_team).show();
  });

  $("#right").on("click", function() {
    $("#team-"+curr_team).hide();
    $("#team-title-"+curr_team).hide();

    var new_team = curr_team + 1;
    if (new_team == 6) {
      new_team = 1;

    }
    curr_team = new_team;
    $("#team-"+new_team).show();
    $("#team-title-"+new_team).show();
  });

  //nature tooltip
  $('.ntooltip').hover( function() {
    var nature = "" + $(this).html().split(" ")[0].slice(0, -1);
    if (nature != "None") {
      if (nature.split('/').length == 2) {
        nature = nature.split('/');
        var str='';


        for (var i = 0; i < 2; i++) {
          if (!(str.includes(natureStats[nature[i]]['increase']))) {
            if ( i > 0) {
              str += ' <br/>↑ ' + natureStats[nature[i]]['increase'];
            } else {
              str += ' ↑ ' + natureStats[nature[i]]['increase'];
            }


          } else {
            str = str.replace('↑', '↑↑');
          }

          if (!(str.includes(natureStats[nature[i]]['decrease']))) {
            str += '<br/> ↓ ' + natureStats[nature[i]]['decrease'];

          } else {
            str = str.replace('↓', '↓↓');
          }
        }
      } else {
        // var str = "Increases: " + natureStats[nature]['increase'] + "<br/>Decreases: " + natureStats[nature]['decrease'];
        var str = "↑ " + natureStats[nature]['increase'] + "<br/>↓ " + natureStats[nature]['decrease'] ;
        // $(this).children[0].attr('id', 'nature_focus');
        // $('#nature_focus').html(str);
      }
      $($(this).children()[0]).html(str);
    } else {
      $($(this).children()[0]).css('background-color', "#fff");
    }





  });


  //for getting move information
  var json;
  $.getJSON("/static/data/allmove_data1.json", function(json_1) {
    $.getJSON("/static/data/allmove_data2.json", function(json_2) {
      $.getJSON("/static/data/allmove_data3.json", function(json_3) {
        $.getJSON("/static/data/allmove_data4.json", function(json_4) {
          $.getJSON("/static/data/allmove_data5.json", function(json_5) {
            $.getJSON("/static/data/allmove_data6.json", function(json_6) {

            json = Object.assign({}, json_1, json_2);
            json = Object.assign({}, json, json_3);
            json = Object.assign({}, json, json_4);
            json = Object.assign({}, json, json_5);
            json = Object.assign({}, json, json_6);

                $(document).on({
                    mouseenter: function () {
                      // console.log("hover");
                      var x = event.clientX;
                      var y = event.clientY;
                      // console.log(x);
                      // console.log(y);
                      // console.log($(window).width());
                      // console.log($(window).height());
                      if (json[$(this).text()]) {
                        var moveData = json[$(this).text()];
                        $(".tooltip-move-title").html($(this).text());
                        $(".tooltip-move-type").html(moveData["type"]);
                        $(".tooltip-move-type").removeClass().addClass("tooltip-move-type").addClass(moveData["type"]);
                        if (moveData["power"]) {
                          $(".tooltip-move-power-value").html(parseInt(moveData["power"]));
                        }
                        else {
                          $(".tooltip-move-power-value").html("-");
                        }
                        if (moveData["accuracy"]) {
                          $(".tooltip-move-accuracy-value").html(parseInt(moveData["accuracy"]));
                        }
                        else {
                          $(".tooltip-move-accuracy-value").html("-");
                        }
                        $(".tooltip-move-description").html(moveData["description"]);
                        $(".tooltip-move-learned-method-value").html(moveData["pokemon"][$.trim($(this).closest(".pokemon-card-name"))])
                        if (x <= $(window).width()/2 && y <= $(window).height()/2) {
                          y = y + $(document).scrollTop();
                          $(".pokemon-move-tooltip").css({top: y, left: x, position:'absolute'});
                        }
                        else if (x <= $(window).width()/2 && y > $(window).height()/2) {
                          y = y - 240 + $(document).scrollTop();
                          $(".pokemon-move-tooltip").css({top: y, left: x, position:'absolute'});
                        }
                        else if (x > $(window).width()/2 && y <= $(window).height()/2) {
                          y = y + $(document).scrollTop();
                          x -= 350;
                          $(".pokemon-move-tooltip").css({top: y, left: x, position:'absolute'});
                        }
                        else {
                          y = y - 240 + $(document).scrollTop();
                          x -= 350;
                          $(".pokemon-move-tooltip").css({top: y, left: x, position:'absolute'});
                        }
                        $(".pokemon-move-tooltip").show();
                      }
                    },
                    mouseleave: function () {
                      // console.log("hover out");
                      $(".pokemon-move-tooltip").hide();
                    }
                }, ".pokemon-move-label");
              });
            });
          });
        });
      });
    });

  //pokeball easter egg
  $('.site-icon').hover( function() {
    $('.site-icon').attr('src', '/static/images/icon4.png');
  });

  $('.site-icon').mouseout( function() {
    $('.site-icon').attr('src', '/static/images/icon3.png');
  });