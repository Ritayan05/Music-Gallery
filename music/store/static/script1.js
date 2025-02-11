function openSearchModal() {
    document.getElementById("search-modal").style.display = "block";
}

function closeSearchModal() {
    document.getElementById("search-modal").style.display = "none";
}

function searchSongs() {
    let query = document.getElementById("search").value;
    let resultsList = document.getElementById("results");

    if (query.length === 0) {
        resultsList.innerHTML = "";
        return;
    }

    fetch(`/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            resultsList.innerHTML = "";
            data.songs.forEach(song => {
                let li = document.createElement("li");
                li.textContent = `${song.title} - ${song.artist}`;
                resultsList.appendChild(li);
            });
        });
}