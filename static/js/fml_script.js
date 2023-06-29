// $(document).ready(function() {

// })


// code given from user on google's issue tracker
// tackles video load failure on first load attempt
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

const popover = new bootstrap.Popover('.btn', {
    container: '.offcanvas-body'
  })

let player = document.getElementById('mvmnt') 

function onStateChange(e) {
    if (e.data === YT.PlayerState.ENDED) {
        player.playVideo();
    }
}

player.addEventListener(onload, onStateChange)