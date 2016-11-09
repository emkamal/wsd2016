// Exercise 2.3 Javascript file  //
// Read the instructions.html //

//some helpful debug code

$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //


$(function() {
    $("a[href$='.pdf']").addClass('pdf');
	
	var allLinks = $("a[href$='.zip']");
	
	var allLinks = $("a");

	allLinks = allLinks.filter(function () {
	  return $(this).attr('href').match(/\.[a-zA-Z0-9]+$/i);
	});
	
	allLinks = allLinks.not(function () {
	  return $(this).attr('href').match(/\.(pdf|html|htm)$/i);
	});
	
	allLinks.addClass('download');
});



// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
