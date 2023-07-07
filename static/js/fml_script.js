// _____________________________________________________________
// as of jquery 3.0, .ready event handler has been deprecated, 
// recommended alternative is now to wrap all code in a function
// https://api.jquery.com/ready/
// _____________________________________________________________
$(function (e) {

    // Edit Profile form labels styling
    $('#id_first_name')[0].labels[0].innerHTML = 'First Name';
    $('#id_last_name')[0].labels[0].innerHTML = 'Last Name';
    
    // footer animation responsiveness on touchscreen devices
    $('footer')[0].on('click', function (e) {
        $('footer')[0].addClass('.footer-touch');
    });

    // 1 Rep Max Related functions
    // Function to apply relevant post "action" to Edit 1RM form
    $('.record-edit').on('click', function (e) {
        let recordId = $(this).attr("id");
        let movementSlug = $('iframe')[0].id;
        $('#edit-record-form').attr('action', `/edit_one_rm/${movementSlug}/${recordId}/`);
    });
      
});