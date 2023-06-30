// _____________________________________________________________
// as of jquery 3.0, .ready event handler has been deprecated, 
// recommended alternative is now to wrap all code in a function
// https://api.jquery.com/ready/
// _____________________________________________________________
$(function (e) {

    // 1 Rep Max Related functions
    // Function to apply relevant post "action" to Edit 1RM form
    $('.record-edit').on('click', function (e) {
        let recordId = $(this).attr("id");
        let movementSlug = document.getElementById('slug').innerHTML;
        $('#edit-record-form').attr('action', `/edit_one_rm/${movementSlug}/${recordId}/`);
    });
      
});