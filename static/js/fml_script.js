// $(document).ready(function() {

// })


// code given from user on google's issue tracker
// tackles video load failure on first load attempt
let player = document.getElementById('mvmnt') 

function onStateChange(e) {
    if (e.data === YT.PlayerState.ENDED) {
        player.playVideo();
    }
}

player.addEventListener(onload, onStateChange)