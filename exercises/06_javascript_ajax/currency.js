$(function(){
  $("#search").on("click", function(e){
    e.preventDefault();

    $.getJSON( "http://api.fixer.io/"+$("#date").val(), function( data ) {
      $("#currencies").html("");
      $.each(data.rates, function(idx, val){
        $("#currencies").append("<tr><td>"+idx+"</td><td>"+val+"</td></tr>");
      });
    });

    // $.ajax({
    //   dataType: "jsonp",
    //   url: "http://api.fixer.io/"+$("#date").val(),
    //   success: function(data){
    //     $("#currencies").html("");
    //     $.each(data.rates, function(idx, val){
    //       $("#currencies").append("<tr><td>"+idx+"</td><td>"+val+"</td></tr>");
    //     });
    //   }
    // });


  })
});
