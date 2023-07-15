$(function () {

    $(`.query`).css('display', 'none');
    $('#library-search').on('keyup', runSearch);
    $('#library-search').val().on('change', runSearch);
    $('#library-search').val().on('change', printVal);

    function runSearch() {
        $(`.query`).css('display', 'none');
        var search = $('#library-search').val();

        let querySet = document.getElementsByClassName('query')

        for (value of querySet) {
            criteriaMatch = false;
            query = value.id;
            query = query.split("-");
            for (word of query) {
                if (word.includes(search)) {
                    criteriaMatch = true
                }
                if (criteriaMatch == true) {
                    document.getElementById(value.id).style.display = 'inline';
                }
            }
        }
    }

    function runSearch() {
        console.log($('#library-search').val();)
    }
});