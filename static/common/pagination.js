function defer() {
    if (window.jQuery){
    	console.log("...........pagination loaded......");
    	pagination_logic();
    	console.log("called the pagination_logic method");
    }
        
    else{
    	console.log('jquery not loaded')
        setTimeout(function() { defer() }, 20);
    }
};
defer();
// The defer is only making sure that the javascript wont run until the jquery is loaded.


console.log(" this should be printed after jquery is loaded");

function pagination_logic(){
    $(document).ready(function(){
	var show_per_page;
	var number_of_items;
	var number_of_pages;
	var navigation_html;
	var current_link;

	function setup(n) {

		console.log ("number of items perpage: " + n);
	
	//how much items per page to show
		show_per_page = n; 
		//getting the amount of elements inside content div
		number_of_items = $('#content').children().size();

		console.log ("number of items: " + number_of_items)
		// console.log(number_of_items);
		//calculate the number of pages we are going to have
		number_of_pages = Math.ceil(number_of_items/show_per_page);

		console.log ("number of pages: " + number_of_pages)
		
		//set the value of our hidden input fields
		$('#current_page').val(0);
		$('#show_per_page').val(show_per_page);	
		navigation_html = ' <a class="previous_link  pagination" class="pagination" href="javascript:previous();">Prev</a>';
	     current_link = 0;

		while(number_of_pages > current_link){
			navigation_html += '<a class="page_link  pagination"  href="javascript:go_to_page(' + current_link +')" longdesc="' + current_link +'"> '+ (current_link + 1) +'</a>  ';
			current_link++;
		}
		navigation_html += ' <a class="next_link pagination" href="javascript:next();">Next</a> ';

		
		$('#page_navigation').html(navigation_html);
		
		//add active_page class to the first page link
		$('#page_navigation .page_link:first').addClass('active_page');
		
		//hide all the elements inside content div
		$('#content').children().css('display', 'none');
		
		//and show the first n (show_per_page) elements
	$('#content').children().slice(0, show_per_page).css('display', 'block');   


	}

	setup(1);

	
	//now when we got all we need for the navigation let's make it '
	
	/* 
	what are we going to have in the navigation?
		- link to previous page
		- links to specific pages
		- link to next page
	*/


	$( "#select_entry" ).change(function() {
	  var sel = Number(this.value);
	  //alert( sel );
	  setup(sel);
	});


	
});
}

function previous(){
	
	new_page = parseInt($('#current_page').val()) - 1;
	//if there is an item before the current active link run the function
	if($('.active_page').prev('.page_link').length==true){
		go_to_page(new_page);
	}
	
}

function next(){
	new_page = parseInt($('#current_page').val()) + 1;
	//if there is an item after the current active link run the function
	if($('.active_page').next('.page_link').length==true){
		go_to_page(new_page);
	}
	
}
function go_to_page(page_num){
	//get the number of items shown per page
	var show_per_page = parseInt($('#show_per_page').val());
	
	//get the element number where to start the slice from
	start_from = page_num * show_per_page;
	
	//get the element number where to end the slice
	end_on = start_from + show_per_page;
	
	//hide all children elements of content div, get specific items and show them
	$('#content').children().css('display', 'none').slice(start_from, end_on).css('display', 'block');
	
	/*get the page link that has longdesc attribute of the current page and add active_page class to it
	and remove that class from previously active page link*/
	$('.page_link[longdesc=' + page_num +']').addClass('active_page').siblings('.active_page').removeClass('active_page');
	
	//update the current page input field
	$('#current_page').val(page_num);
}
  



