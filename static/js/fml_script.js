$(document).ready(function() {

    
    $('.record-edit').click(function(){
        let recordId = $("#" + fieldset_id);
        let movementSlug = $('#slug');
        console.log(`recordId: ${recordId}`);
        console.log(`movementSlug: ${movementSlug}`);
        $('#edit-record-form').attr('action', `/edit_one_rm/${movementSlug}/${recordId}/`);

    });


});

