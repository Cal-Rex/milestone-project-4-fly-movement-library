const MOVEMENT = document.getElementById('video-id').innerHTML;

var player;

    function onYouTubeIframeAPIReady() {
      player = new YT.Player('player', {
        videoId: MOVEMENT,
        events: {
          'onReady': onPlayerReady,
          'onError': onPlayerError
        }
      });
    }

    function onPlayerReady(event) {
      event.target.playVideo();
    }

    function onPlayerError(event) {
      if (event.data === 100 || event.data === 150) {
        player.loadVideoById(MOVEMENT);
      }
    }