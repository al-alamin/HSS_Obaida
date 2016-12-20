function defer() {
    if (window.jQuery){
      console.log("...........titme loaded......");
      timer_logic();

    }
        
    else{
      console.log('jquery not loaded')
        setTimeout(function() { defer() }, 20);
    }
};
defer();

// The defer is only making sure that the javascript wont run until the jquery is loaded.


function timer_logic(){
  jQuery(document).ready(function(){

  var link = document.getElementsByTagName("a")[0];

      link.onclick = function(){
         $('.lightbox').show();
          setTimeout(function(){window.location.href = link.getAttribute("data-url")}, 1000)
      }

  });

  $(function(){
      var count = $("#time").text();
      // console.log("the value of count");
      // console.log(count);

      // alert (count);

      countdown = setInterval(function(){
      min = Math.floor(count/60);
      sec = count % 60;
      // $("#time").html(count + " seconds remaining!");

      $("#time").html(min + " Minute " + sec + " Second Remaining");
      

      if (count <= 0) {
        // window.location = 'http://google.com';
        console.log("about the submit the form");
        $("form").submit();
    //     $("form").submit(function(){
    //     alert("Submitted");
    // });
      }
      count--;
    }, 1000);
  });
}
