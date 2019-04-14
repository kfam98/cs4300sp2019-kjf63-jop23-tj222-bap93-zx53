// function updateTimelines() {
//   var height = $('.trump-timeline').height();
//   var heightString = height.toString() + 'px';
//   var checkExist = setInterval(function() {
//      if ($('#twitter-widget-1').length) {
//         // alert("Exists!");
//         if($("#twitter-widget-1").height()>0) {
//           // alert($("#twitter-widget-0").height());
//           $("#twitter-widget-0").css('height', heightString);
//           $("#twitter-widget-1").css('height', heightString);
//           clearInterval(checkExist);
//         }
//      }
//   }, 100);
// };

// function updateTimelines() {
//   var height = $('.trump-timeline').height();
//   var heightString = height.toString() + 'px';
//   var checkExist = setInterval(function() {
//      if ($('iframe.twitter-timeline').length) {
//         // alert("Exists!");
//         if($("iframe.twitter-timeline").height()>0) {
//           // alert($("#twitter-widget-0").height());
//           $("iframe.twitter-timeline").css('height', heightString);
//           clearInterval(checkExist);
//         }
//      }
//   }, 100);
// };

$(document).ready(function() {
    // updateTimelines();

    // var height = $('.trump-timeline').height();
    // var heightString = height.toString() + 'px';
    // var checkExist = setInterval(function() {
    //    if ($('#twitter-widget-1').length) {
    //       // alert("Exists!");
    //       if($("#twitter-widget-1").height()>0) {
    //         // alert($("#twitter-widget-0").height());
    //         $("#twitter-widget-0").css('height', heightString);
    //         $("#twitter-widget-1").css('height', heightString);
    //         clearInterval(checkExist);
    //       }
    //    }
    // }, 100);

    // alert($("#twitter-widget-0").delay(1000).height());

    // $('iframe.twitter-timeline').css('min-height', '1000px!important;');

    // $(".iframe.twitter-timeline").css("height","500");

    // alert(height);
    // alert(height);
    // $('.trump-timeline>.twitter-timeline').attr('data-height', height);

    // $('.trump-timeline').empty();
    // var htmlString = '<a class="twitter-timeline" href="https://twitter.com/realDonaldTrump" data-height="' + height.toString() + '"> Tweets by @realDonaldTrump </a>';
    // htmlString += "<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+" + '"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>';
    // htmlString += '<script id="twitter-wjs" type="text/javascript" async defer src="//platform.twitter.com/widgets.js"></script>';
    // $('.trump-timeline').html(htmlString);

    //
    // $('.location-select').select2({
    //   minimumInputLength: 0
    // });
    //
    // $('#location-select-form').on('submit', function(e) {
    //     e.preventDefault();
    //     $.ajax({
    //         url : $(this).attr('action') || window.location.pathname,
    //         type: "GET",
    //         data: $(this).serialize(),
    //         success: function (data) {
    //             $("#form_output").html(data);
    //         },
    //         error: function (jXHR, textStatus, errorThrown) {
    //             alert(errorThrown);
    //         }
    //     });
    // });

    // $("#location-select").on("change", function() {
    //     var $this = $(this);
    //     alert($this.val());
        // console.log('autosubmitting');
        // if (!currentData || currentData != $this.val()) {
        //     $($this.get(0).form).ajaxSubmit(function (response, status, xhr, $form) {
        //         currentData = "";
        //     });
        // }
    // });

    // $('#location-select-form').on('submit', function(e) {
    //     e.preventDefault();
    //     $.ajax({
    //         url : $(this).attr('action') || window.location.pathname,
    //         type: "GET",
    //         data: $(this).serialize(),
    //         success: function (data) {
    //             $("#form_output").html(data);
    //         },
    //         error: function (jXHR, textStatus, errorThrown) {
    //             alert(errorThrown);
    //         }
    //     });
    // });

    // var frm = $('#location-select-form');
    // frm.submit(function (ev) {
    //     $.ajax({
    //         type: frm.attr('method'),
    //         url: frm.attr('action'),
    //         data: frm.serialize(),
    //         success: function (data) {
    //             alert('ok');
    //         }
    //     });
    //
    //     ev.preventDefault();
    // });


});
