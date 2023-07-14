// _____________________________________________________________
// as of jquery 3.0, .ready event handler has been deprecated, 
// recommended alternative is now to wrap all code in a function
// https://api.jquery.com/ready/
// _____________________________________________________________
$(function () {

    // function to timeout system messages
    setTimeout(function() {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);

    // book a class panel hover response
    $('#book-a-class').on('mouseenter', function() {
        $('#book-a-class-btn').addClass('js-psuedo-hover');
    });
    $('#book-a-class').on('mouseleave', function() {
        $('#book-a-class-btn').removeClass('js-psuedo-hover');
    });

    // 1 Rep Max Related functions
    // Function to apply relevant post "action" to Edit 1RM form
    $('.record-edit').on('click', function () {
        let recordId = $(this).attr("id");
        let movementSlug = $('iframe')[0].id;
        $('#edit-record-form').attr('action', `/edit_one_rm/${movementSlug}/${recordId}/`);
        $('.edit-rm-oc-label')[0].innerHTML = "Edit 1-RM from:<br>" + $(`.${recordId}`)[0].innerHTML;

        console.log($(`.${recordId}`)[0].innerHTML);
    });

    let iconIdentify = $('.footer-icon')[0];
    
    // footer hover animations
    // animation class taken from Font-Awesome
    $('.footer-icon:first').on('mouseenter', function () {
        $('.footer-icon:first').addClass('fa-beat');
    });
    $('.footer-icon:first').on('mouseleave', function () {
        $('.footer-icon:first').removeClass('fa-beat');
    });
    $('.footer-icon:last').on('mouseenter', function () {
        $('.footer-icon:last').addClass('fa-beat');
    });
    $('.footer-icon:last').on('mouseleave', function () {
        $('.footer-icon:last').removeClass('fa-beat');
    });
    $('.fly-icon:first').on('mouseenter', function () {
        $('.fly-icon:first').addClass('fa-beat');
    });
    $('.fly-icon:first').on('mouseleave', function () {
        $('.fly-icon:first').removeClass('fa-beat');
    });
    
    // footer animation responsiveness on touchscreen devices
    // $('footer')[0].on('click', function (e) {
    //     $('footer')[0].addClass('.footer-touch');
    // });
});