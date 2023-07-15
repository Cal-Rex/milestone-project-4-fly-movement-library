$(function () {
    
    let libraryList = $('.query');
    // for (movement of $('.query')) {
    //     console.log(movement)
    let i = 0
    for (movement of libraryList){
        $(`#${libraryList[i].id}`).css('display', 'none');
        var object = $(`#${libraryList[i].id}`).attr('id')
        // console.log($(`#${object}`).attr('id'))
        var object = object;
        // console.log(document.getElementById(object).innerText);
        // console.log(object)

        i++
        // console.log(libraryList[i].id)
    };
    $('#library-search').on('keyup', function () {
        let search = $('#library-search').val();
        console.log(search);
        i = 0
        for (movement of libraryList){
            $(`#${libraryList[i].id}`).css('display', 'none');
            var object = $(`#${libraryList[i].id}`).attr('id')
            // console.log(document.getElementById(object).innerText);
            var searchArray = document.getElementById(object).innerText.split(" ").filter(entry => entry !== "");
            var searchArray = searchArray.filter(entry => entry !== "\n");
            for (value of searchArray) {
                console.log("searchArray value:", value);
                if (value.includes(search)){
                    document.getElementById(object).style.display = "inline";
                }
            }

            // var deSpacedArray = searchArray.filter();
            // console.log(searchArray);



            // console.log(document.getElementById(object).innerText)
            if (document.getElementById(object).innerHTML.includes(search)) {
                document.getElementById(object).style.display = "inline";
            }
            i++
        }
            // if ($('.query')[movement].innerText.includes(search)) {
            //     $('.query')[movement].css('display', 'inline');
            // }
            // else {
            //     $('.query')[movement].css('display', 'none');
            // }
});
    
    



});