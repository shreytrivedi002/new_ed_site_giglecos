$(document).ready(function() {
    $("#tsrat").click(function() {
        $.ajax({
            url: "https://gilecos.herokuapp.com/ajaxCheck/",
            data: {
                'email_': $('#studentEmail').val(),

            },

            success: function(result) {
                $("#div1").html(result['response']);
                // alert(result['response']);
                console.log(result)
                $('#studentEmail').val('');


            },
            error: function(result) {
                $('#div1').html('<h3>Either you did not paid/Enrolled for any Courses <br> <br> or if You already paid/enrolled <br> <br> Some Unexpected Error Occured... Try reporting the Error</h3>');
            }
        });
    });




    $('.owl-carousel').owlCarousel({
        loop: true,
        items: 3,
        autoplay: true,
        autoplayTimeout: 1000,
        autoplayHoverPause: true,
        stagePadding: 50,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            600: {
                items: 3,
                nav: false
            },
            720: {
                items: 4,
                nav: true
            },
            1000: {
                items: 5,
                nav: true,
                loop: true
            }
        }
    })





});