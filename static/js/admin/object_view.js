// Codigo para crar el emparejamiento del torneo, se usa en object_view.html
document.getElementById('create_tournament').addEventListener('click', function () {
    fetch('tournament_matches/')
    .then((response) => response.json()) 
    .then((data) => {
        const matches_list = document.getElementById('matches__list')
        matches_list.innerHTML = ''
        data.matches.forEach((match) => {
            let current_match = `<div class="match" id="match_${match.id}"><h4>${match.id}</h4>
            <div class="match__jugadores"><p class="player">${match.player1}</p>  <p>vs</p> <p class="player">${match.player2}</p></div>
            </div>`;
        matches_list.innerHTML += current_match;
        })
    })
})

// Cambiar la url para que la redirija al change
const change_link = document.getElementById('change_info')
if (change_link){
    const current_url = change_link.href;
    console.log(current_url);
    const new_url = current_url.replace("/view/#", "/change");
    console.log(new_url);
    change_link.href = new_url;
}

