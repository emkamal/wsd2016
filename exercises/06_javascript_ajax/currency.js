$(function(){
  $("#search").on("click", function(e){
    e.preventDefault();

    $.ajax({
      dataType: "json",
      url: "http://api.fixer.io/"+$("#date").val(),
      success: function(data){
        $("#currencies").html("");
        $.each(data.rates, function(idx, val){
          $("#currencies").append("<tr><td>"+idx+"</td><td>"+val+"</td></tr>");
        });
      }
    });
  })
});
