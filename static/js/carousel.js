var owl = $('.custom-carousel');
owl.owlCarousel({

    autoWidth: true,
    loop: true,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true
    
});



$(document).ready(function () {
    $(".custom-carousel .item").click(function () {
       
        $(".custom-carousel .item").not($(this)).removeClass("active");
        $(this).toggleClass("active");
    });
});
