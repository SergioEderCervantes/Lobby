// ------------------------------------ Miscelaneos ------------------------------------

//Clase para manejar las puntuaciones de los jugadores Round Robin
class Player {
    constructor(name) {
        this.name = name;
        this.wins = 0;
        this.losses = 0;
        this.ties = 0;
        this.points = 0;
        this.goals = 0;
        this.againistGoals = 0;
    }
}

// Cambiar la url para que la redirija al change
const change_link = document.getElementById('change_info')
if (change_link) {
    const current_url = change_link.href;
    console.log(current_url);
    const new_url = current_url.replace("/view/#", "/change");
    console.log(new_url);
    change_link.href = new_url;
}


// ------------------------------------Parte que maneja los eventos de Puntuacion------------------------------------
const svg = document.getElementById("svg_enfrentamientos");
const tournamentType = svg.classList[0]; //Clase Round
if(tournamentType == 'Round') calculateSVGStats();

let puntuationEnteredBand = checkPuntuationsEntered();
if (puntuationEnteredBand){
    document.getElementById('reset__button').classList.remove('hide');
}
// Funcion que busca entre todos los matchups para encontrar si el svg tiene algun valor (los matchups tienen puntuacion),
// Devuelve true si existe ya aunque sea un matchup con puntuacion, false si no
function checkPuntuationsEntered() {
    const seleccionableRectPlayer1 = document.querySelectorAll(".match__puntaje__player1__text");
    const seleccionableRectPlayer2 = document.querySelectorAll(".match__puntaje__player2__text");
    const seleccionableRectPlayers = [...seleccionableRectPlayer1, ...seleccionableRectPlayer2]
    const resultado = seleccionableRectPlayers.some((text) => {
        return text.textContent != ""
    });
    return resultado;
}

document.querySelectorAll(".match__puntaje__player1").forEach((rect) => {
    rect.addEventListener('click', (event) => activateInput(event.target, 1))
});
document.querySelectorAll(".match__puntaje__player2").forEach((rect) => {
    rect.addEventListener('click', (event) => activateInput(event.target, 2))
});

function activateInput(target, playerNum) {
    // Primero que nada, evaluar si tiene un jugador real referenciado o es un valor de id de match
    const matchGroup = target.closest('g');
    const playerClassName = playerNum == 1 ? ".matchup__player1" : ".matchup__player2";
    aux = "";
    // si tiene un numero, no hacer nada
    if(isDigit( matchGroup.querySelector(playerClassName).textContent)){
        return;
    }
    const className = playerNum == 1 ? ".match__puntaje__player1__text" : ".match__puntaje__player2__text";
    const matchText = matchGroup.querySelector(className);
    const inputField = document.getElementById("svg_input");
    
    //Cuando se hace click dentro de un campo con un numero ya ingresado, se elimina el numero para mejorar la visualización
    if(isDigit(matchText.textContent)) {
        aux = matchText.textContent
        matchText.textContent = ""; 
    }
    // Pocisionar el input en donde se dio el click
    const rect = target.getBoundingClientRect();
    inputField.style.left = `${rect.left + window.scrollX}px`;
    inputField.style.top = `${rect.top + window.scrollY}px`;

    // Mostrar el input
    //inputField.value = matchText.textContent;
    inputField.value;
    inputField.style.display = 'block';
    inputField.focus();

    // Actualizar texto
    inputField.onblur = () => {
        if(inputField.value != "") {
            inputField.value = "";
        }
        //Mostrar nuevamente valor cuando se pierde el foco
        if(aux != "" && matchText.textContent == "") {
            inputField.value = aux;
            aux = "";
            putPuntuationValue(inputField, matchText, matchGroup);
        }
    }
    inputField.onkeyup = (e) => {
        if (e.key === 'Enter') {
            e.preventDefault(); // Asegurarnos de que no haya un comportamiento no deseado con Enter
            putPuntuationValue(inputField, matchText, matchGroup);
        }

    }
}
// NOTE = no se como vaya a estar esta vaina
const MAX_PUNTAJE = 100; 
function putPuntuationValue(inputField, matchText, parentGroup) {
    inputField.style.display = "none";
    // Validacion si se envia una cadena vacia
    if (inputField.value === "") {
        return;
    }
    // Validacion de numeros negativos
    if (inputField.value < 0){
        return;
    }
    // Validar que no sea winner o loser
    if (matchText.classList.contains('winner') || matchText.classList.contains('loser')){
        inputField.value = "";
        return;
    }
    // validacion de Maximos
    if (inputField.value > MAX_PUNTAJE){
        inputField.value = MAX_PUNTAJE
    }
    // Cambio de valores del DOM
    matchText.textContent = inputField.value;
    inputField.value = "";
    puntuationEnteredBand = true;

    // Aparecer los botones de opciones
    document.getElementById('send__button').classList.remove('hide');
    document.getElementById('cancel__button').classList.remove('hide');
    document.getElementById('reset__button').classList.remove('hide');
    
    // Comprobar si ya hay valores en ambos lados
    const puntaje1 = parentGroup.querySelector(".match__puntaje__player1__text").textContent;
    const puntaje2 = parentGroup.querySelector(".match__puntaje__player2__text").textContent;
    if (puntaje1 != "" && puntaje2 != "") {
        const players = parentGroup.querySelectorAll('.matchup__player1, .matchup__player2');
        let changeBand = false; //bandera para cuando hay cambio de resultados en el match
        players.forEach(player => {
            // Verifica si el elemento tiene la clase 'winner' y la elimina
            if (player.classList.contains('winner')) {
                player.classList.remove('winner');
                changeBand = true;
            }
        
            // Verifica si el elemento tiene la clase 'loser' y la elimina
            if (player.classList.contains('loser')) {
                player.classList.remove('loser');
                changeBand = true;
            }

            // Verifica si el elemento tiene la clase 'tie' y la elimina
            if (player.classList.contains('tie')) {
                player.classList.remove('tie');
                changeBand = true;
            }
        });
        if(tournamentType == "Round") {
            calculatePuntuation(puntaje1, puntaje2, parentGroup, changeBand);
        } else {
            playerToNextMatch(puntaje1, puntaje2, parentGroup, changeBand);
        }
    }  
}

// Funcion que maneja la logica cuando ya se introdujeron los dos puntajes de los players y uno debe de pasar a la siguente ronda
function playerToNextMatch(puntaje1, puntaje2, parentGroup, changeBand) {
    const intPuntaje1 = parseInt(puntaje1)
    const intPuntaje2 = parseInt(puntaje2)
    const matchId = parentGroup.id.split("__")[1];
    // Validacion de empate 
    if (intPuntaje1 == intPuntaje2) {
        // TODO: mostrar tooltip de error, en un torneo de eliminacion directa no hay empates
        return
    }
    
    let ganador;
    let perdedor;
    if (intPuntaje1 > intPuntaje2){
        ganador = parentGroup.querySelector(".matchup__player1");
        perdedor = parentGroup.querySelector(".matchup__player2");
    }
    else{
        ganador = parentGroup.querySelector(".matchup__player2");
        perdedor = parentGroup.querySelector(".matchup__player1");
    }
    ganador.classList.add('winner');
    perdedor.classList.add('loser');
    const nextPlayerPlace= findPlayerInOtherMatch(matchId);
    // Sabiendo el jugador del matchup, ponemos el nombre del ganador en vez del id del matchup
    nextPlayerPlace.textContent = ganador.textContent;
    nextPlayerPlace.classList.add('changed', matchId);
}

// Devuelve el elemento text del DOM que tenga el idToSearch como player
function findPlayerInOtherMatch(idToSearch) {
    const matchups = svg.querySelectorAll(".matchup");
    let result;
    for (let i = 0; i < matchups.length; i++) {
        const element = matchups[i];

        if(element.querySelector(".matchup__player1").classList.contains(idToSearch)) { 
            result = element.querySelector(".matchup__player1");
            break;     
        }
        if(element.querySelector(".matchup__player2").classList.contains(idToSearch)) {
            result = element.querySelector(".matchup__player2");
            break;
        }
        if (element.querySelector(".matchup__player1").textContent == idToSearch){
            result = element.querySelector(".matchup__player1");
            break;
        }
        if (element.querySelector(".matchup__player2").textContent == idToSearch){
            result = element.querySelector(".matchup__player2");
            break;
        }
    }

    if (result == null){
        console.log("No encontro ningun matchup con un jugador =" + idToSearch);
    }

    return result;
}


function resetPuntajes(){
    // Quitar puntajes
    svg.querySelectorAll(".match__puntaje__player1__text").forEach((element) => element.textContent = "");
    svg.querySelectorAll(".match__puntaje__player2__text").forEach((element) => element.textContent = "");
    // Quitar los jugadores que habian avanzado al siguiente match
    const players = svg.querySelectorAll(".matchup__player");
    const changed = svg.querySelectorAll(".changed");
    if (changed.length > 0){
        regresarPlayers(players,changed);
    }
    
    // Quitar winners y losers
    svg.querySelectorAll(".matchup__player1").forEach((element) => element.classList.remove('winner','loser', 'tie'));
    svg.querySelectorAll(".matchup__player2").forEach((element) => element.classList.remove('winner','loser', 'tie'));
}

function regresarPlayers(players, changed){
    const arrayPlayers = Array.from(players);
    const arrayChanged = Array.from (changed);
    arrayChanged.reverse();
    arrayPlayers.reverse();
    arrayChanged.forEach((changedElement) => {
        const text = changedElement.textContent;
        const playerOriginal = arrayPlayers.find((player) =>{
            return (
                player.querySelector("text").textContent == text &&
                player !== changedElement.closest(".matchup__player")
            )
        })  
        const id = playerOriginal.closest('.matchup').id;
        changedElement.textContent = id.split("__")[1];

        changedElement.classList.remove('changed');
    })
}

//Función que hace el calculo de puntuaciones para Round Robin
function calculatePuntuation(puntaje1, puntaje2, parentGroup, changeBand) {
    const intPuntaje1 = parseInt(puntaje1)
    const intPuntaje2 = parseInt(puntaje2)
    const player1 = new Player(parentGroup.querySelector(".matchup__player1").textContent);
    const player2 = new Player(parentGroup.querySelector(".matchup__player2").textContent);
    const matchId = parentGroup.id.split("__")[1];
    // Validacion de empate 
    if (intPuntaje1 == intPuntaje2) {
        // Agregamos la clase empate a los jugadores 
        parentGroup.querySelector(".matchup__player1").classList.add('tie');
        parentGroup.querySelector(".matchup__player2").classList.add('tie');
        player1.ties = 1;
        player2.ties = 1;
    } else {
        
        let ganador;
        let perdedor;
        if (intPuntaje1 > intPuntaje2){
            ganador = parentGroup.querySelector(".matchup__player1");
            perdedor = parentGroup.querySelector(".matchup__player2");
            player1.wins = 1;
            player2.losses = 1;
        }
        else{
            ganador = parentGroup.querySelector(".matchup__player2");
            perdedor = parentGroup.querySelector(".matchup__player1");
            player2.wins = 1;
            player1.losses = 1;
        }
        ganador.classList.add('winner');
        perdedor.classList.add('loser');
    }
    player1.goals = parseInt(parentGroup.querySelector(".match__puntaje__player1__text").textContent);
    player1.againistGoals = parseInt(parentGroup.querySelector(".match__puntaje__player2__text").textContent);
    player2.goals = parseInt(parentGroup.querySelector(".match__puntaje__player2__text").textContent);
    player2.againistGoals = parseInt(parentGroup.querySelector(".match__puntaje__player1__text").textContent);
   
    if(changeBand) {
        calculateSVGStats()
    } else {
        modificateTable(player1);
        modificateTable(player2);
    }
}

//Función que modifica la tabla de resultados 
function modificateTable(player) {
    const tableRows = document.querySelectorAll('#standings_table tbody tr');
        
    //Busca en la tabla a los jugadores para modificar sus estadisticas
    tableRows.forEach(row => {
            
        if(player.name == row.querySelector('td:nth-child(2)').textContent) {
            player.wins += parseInt(row.querySelector('td:nth-child(3)').textContent);   // Partidos ganados
            player.losses += parseInt(row.querySelector('td:nth-child(4)').textContent); // Partidos perdidos
            player.ties += parseInt(row.querySelector('td:nth-child(5)').textContent); // Partidos empatados
            player.goals += parseInt(row.querySelector('td:nth-child(7)').textContent); // goles totales
            player.againistGoals += parseInt(row.querySelector('td:nth-child(8)').textContent);
            
            updatePlayerStats(player.name, player.wins, player.losses, player.ties, player.wins * 3 + player.ties, player.goals, player.againistGoals);
        }
    });
}

// Función para modificar los datos de un jugador
function updatePlayerStats(playerName, newWon, newLost, newDraw, newPoints, newGoals, newAgainistGoals) {
    const tableRows = document.querySelectorAll('#standings_table tbody tr');
    
    tableRows.forEach(row => {
        const name = row.querySelector('td:nth-child(2)').textContent;  // Nombre del jugador
        if (name === playerName) {
            row.querySelector('td:nth-child(3)').textContent = newWon;  // Actualiza partidos ganados
            row.querySelector('td:nth-child(4)').textContent = newLost; // Actualiza partidos perdidos
            row.querySelector('td:nth-child(5)').textContent = newDraw; // Actualiza partidos empatados
            row.querySelector('td:nth-child(6)').textContent = newPoints; // Actualiza puntos de juego
            row.querySelector('td:nth-child(7)').textContent = newGoals; // Actualiza goles a favor
            row.querySelector('td:nth-child(8)').textContent = newAgainistGoals; // Actualiza goles en contra
            if(newGoals - newAgainistGoals >= 0)
                row.querySelector('td:nth-child(9)').textContent = newGoals - newAgainistGoals; // Actualiza diferencia de goles
            else   
            row.querySelector('td:nth-child(9)').textContent = newAgainistGoals - newGoals;

        }
    });
    sortTable();
}

// Función para ordenar la tabla por partidos ganados
function sortTable() {
    const table = document.getElementById("standings_table");
    const rows = Array.from(table.querySelectorAll("tbody tr"));
    
    rows.sort((rowA, rowB) => {
        const puntajeA = parseInt(rowA.cells[5].textContent);  // Obtener los partidos ganados de la fila A
        const puntajeB = parseInt(rowB.cells[5].textContent);  // Obtener los partidos ganados de la fila B

        const golesA = parseInt(rowA.cells[8].textContent); // diferencia de goles
        const golesB = parseInt(rowB.cells[8].textContent); // diferencia de goles


        // Ordenar por puntaje (descendente)
        if (puntajeB !== puntajeA) {
            return puntajeB - puntajeA;
        }

        // Si los puntajes son iguales, ordenar por goles (descendente)
        return golesB - golesA;
    });

    // Reordenar las filas en el cuerpo de la tabla
    const tbody = table.querySelector("tbody");
    rows.forEach(row => tbody.appendChild(row));

    // Actualizar el ranking
    updateRanking();
}

// Función para actualizar los números de ranking después de ordenar
function updateRanking() {
    const table = document.getElementById("standings_table");
    const rows = table.querySelectorAll("tbody tr");

    rows.forEach((row, index) => {
        row.cells[0].textContent = index + 1; // Actualiza la posición de ranking
    });
}

//Función para contar el numero de partidos ganados, perdidos y empatados dentro del SVG
function calculateSVGStats() {
    const playersMap = new Map(); // Usamos un mapa para evitar duplicados y acceder rápido por nombre

    // Recorrer los jugadores en los textos de clase "matchup__player1" y "matchup__player2"
    const playerTexts = document.querySelectorAll(".matchup__player1, .matchup__player2");

    playerTexts.forEach(playerText => {
        const name = playerText.textContent.trim();
        const parentGroup = playerText.closest(".matchup");

        // Si no existe en el mapa, agregar un nuevo jugador
        if (!playersMap.has(name)) {
            playersMap.set(name, new Player(name));
        }

        const player = playersMap.get(name);

        // Incrementar contadores según la clase del texto
        if (playerText.classList.contains("winner")) {
            player.wins++;
        } else if (playerText.classList.contains("loser")) {
            player.losses++;
        } else if (playerText.classList.contains("tie")) {
            player.ties++;
        }

        // Obtener los goles desde la clase "match__puntaje__playerX__text"
        let playerIndex;
        let oponentIndex = playerText.classList.contains("matchup__player1") ? 1 : 2;
        if(playerText.classList.contains("matchup__player1")){
            playerIndex = 1;
            oponentIndex = 2;
        }
        else {
            playerIndex = 2;
            oponentIndex = 1;
        }
        const goalsText = parentGroup.querySelector(`.match__puntaje__player${playerIndex}__text`);
        const goalsOpponentText = parentGroup.querySelector(`.match__puntaje__player${oponentIndex}__text`);
        if (goalsText) {
            player.goals += parseInt(goalsText.textContent.trim()) || 0; // Sumar goles, o 0 si no hay un número válido
        }
        if (goalsOpponentText) {
            player.againistGoals += parseInt(goalsOpponentText.textContent.trim()) || 0; // Sumar goles, o 0 si no hay un número válido
        }
        updatePlayerStats(player.name, player.wins, player.losses, player.ties, player.wins * 3 + player.ties, player.goals, player.againistGoals);
    });
}

function isDigit(str) {
    return !isNaN(str) && !isNaN(parseInt(str));
}
// ------------------------------------Parte que maneja los eventos de Drag------------------------------------
const nodes = [];
svg.addEventListener('load', function () {
    const draw = SVG('#svg_enfrentamientos')

    draw.find('.draggable').forEach(element => {
        nodes.push(element.node);


        element.draggable();
        // Opcional: Añadir eventos para monitorear el arrastre
        element.on('dragstart', (event) => dragstart(event, element));

        element.on('dragend', (event) => dragEnd(event, element));
    })

});
let switched = false;
let prevXText = 0;
let prevYText = 0;
let prevX = 0;
let prevY = 0;
let prevNode = null
function dragstart(event, element) {
    const node = element.node;
    const rect = node.querySelector("rect");
    const text = node.querySelector("text");
    prevXText = text.getAttribute('x');
    prevYText = text.getAttribute('y');
    prevX = rect.getAttribute('x');
    prevY = rect.getAttribute('y');
    prevNode = node;
}

function dragEnd(event, element) {
    // Si se metio puntajes, no hacer swap
    if (puntuationEnteredBand) {
        // TODO: show tooltip
        backRect(element)
    }
    const newSvgSquare = SVG(element.node.querySelector("rect"));

    const nodeToSwitch = nodes.find(nodo => {
        let rectangulo = SVG(nodo.querySelector("rect"));
        return isNear(rectangulo, newSvgSquare, 20);
    });

    switched = nodeToSwitch != undefined

    if (switched) {
        // Hacer el switch
        const aux = prevNode.querySelector("text").textContent;
        prevNode.querySelector("text").textContent = nodeToSwitch.querySelector("text").textContent;
        nodeToSwitch.querySelector("text").textContent = aux;
        // Que el boton de guardar y cancelar aparezca
        document.getElementById('send__button').classList.remove('hide');
        document.getElementById('cancel__button').classList.remove('hide');


    }

    //Regresar el elemento a su posicion original
    backRect(element)

}

// Funcion que regresa el rectangulo al mismo lugar donde estaba
function backRect(element) {
    const node = element.node;
    const rect = node.querySelector("rect");
    const text = node.querySelector("text");
    rect.setAttribute('x', prevX);
    rect.setAttribute('y', prevY);
    text.setAttribute('x', prevXText);
    text.setAttribute('y', prevYText);
}


function isNear(el1, el2, proximityTreshold) {
    const width = parseInt(el1.width(), 10);
    const height = parseInt(el1.height(), 10);
    const center1 = { x: el1.x() + width / 2, y: el1.y() + height / 2 };
    const center2 = { x: el2.x() + width / 2, y: el2.y() + height / 2 };
    return (
        (Math.abs(center1.x - center2.x) < proximityTreshold) && (Math.abs(center1.y - center2.y) < proximityTreshold) && (el1 !== el2)
    );
}



// --------------------------Parte que Maneja el Boton de guardar si hubo modificaciones al svg----------------


document.getElementById('send__button').addEventListener('click', function () {
    const draw = SVG('#svg_enfrentamientos');
    send_SVG(draw, csrfToken, tournamentId);
    this.classList.add('hide');
    document.getElementById("cancel__button").classList.add('hide');
});
document.getElementById('cancel__button').addEventListener('click', function () {
    location.reload();
});
document.getElementById('reset__button').addEventListener('click',function (){
    resetPuntajes();
    puntuationEnteredBand = false;
    this.classList.add('hide');
    document.getElementById('send__button').classList.remove('hide');
    document.getElementById('cancel__button').classList.remove('hide');

})


// ------------------------------------Parte que manda el SVG de vuelta al server------------------------------

// Funcion que manda el svg al servidor, se llama cuando ocurre una modificacion en el svg, sobretodo el cambio de jugadores
// Espera una instancia de SVG.js, el csrf_token y el id del torneo
async function send_SVG(draw, csrf_token, torneo_id) {
    const svgElement = draw.node;
    const svgData = svgElement.outerHTML;


    try {
        const response = await fetch('/admin/save_svg/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token
            },
            body: JSON.stringify({
                svg_data: svgData,
                torneo_id: torneo_id
            }),
        });

        if (response.ok) {
            console.log("SVG enviado correctamente.");
        } else {

            console.log("Hubo un problema al enviar el SVG.");
        }

    }
    catch (error) {
        console.error("Error en la solicitud:", error);
    }
}