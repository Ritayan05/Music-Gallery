
const playlist = [
    {
        title: 'Song 1',
        artist: 'Artist 1',
        image: '{% static "image/chill.jpg" %}',
        audio: '{% static "audio/song1.mp3" %}',
    },
    {
        title: 'Song 2',
        artist: 'Artist 2',
        image: '{% static "image/chill.jpg" %}',
        // audio: '{% static "audio/song2.mp3" %}',
    },
    {
        title: 'Song 3',
        artist: 'Artist 3',
        image: '{% static "image/chill.jpg" %}',
        // audio: '{% static "audio/song3.mp3" %}',
    }
];

const playlistContainer = document.getElementById('playlist');
const playButton = document.getElementById('play');
const previousButton = document.getElementById('previous');
const nextButton = document.getElementById('next');
const currentSongTitle = document.getElementById('currentSongTitle');
const currentSongArtist = document.getElementById('currentSongArtist');
const audioElement = new Audio();

let currentSongIndex = 0;

function loadSong(songIndex) {
    const song = playlist[songIndex];
    currentSongTitle.textContent = song.title;
    currentSongArtist.textContent = song.artist;
    audioElement.src = song.audio;
    document.getElementById('playlist').innerHTML = `
        <li>
            <image class="invert" src="${song.image}" alt="song-image" width="50"> ${song.title}
        </li>
    `;
}

function playPauseSong() {
    if (audioElement.paused) {
        audioElement.play();
        playButton.src = "{% static 'image/pause.svg' %}";
    } else {
        audioElement.pause();
        playButton.src = "{% static 'image/play.svg' %}";
    }
}

function nextSong() {
    currentSongIndex = (currentSongIndex + 1) % playlist.length;
    loadSong(currentSongIndex);
    audioElement.play();
}

function previousSong() {
    currentSongIndex = (currentSongIndex - 1 + playlist.length) % playlist.length;
    loadSong(currentSongIndex);
    audioElement.play();
}

audioElement.addEventListener('ended', nextSong);

playButton.addEventListener('click', playPauseSong);
nextButton.addEventListener('click', nextSong);
previousButton.addEventListener('click', previousSong);

loadSong(currentSongIndex);
