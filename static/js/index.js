$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      loop:true,
      responsiveClass:true,
      autoplay:true,
      autoplayTimeout:2500,
      autoplayHoverPause:true,
      responsive:{
        0:{
          margin:10,  
          items:1
        },
        600:{
          margin:20,
          items:2
        },
        1000:{
          margin:40,
          items:3
        }
      }
    });
  });

 