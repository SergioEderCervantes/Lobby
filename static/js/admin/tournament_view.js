// ------------------------------------ Miscelaneos ------------------------------------


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
    const aux =  matchGroup.querySelector(playerClassName);
    // si tiene un numero, no hacer nada
    if(isDigit( matchGroup.querySelector(playerClassName).textContent)){
        return;
    }
    const className = playerNum == 1 ? ".match__puntaje__player1__text" : ".match__puntaje__player2__text";
    const matchText = matchGroup.querySelector(className);
    
    const inputField = document.getElementById("svg_input")
    // Pocisionar el input en donde se dio el click
    const rect = target.getBoundingClientRect();
    inputField.style.left = `${rect.left + window.scrollX}px`;
    inputField.style.top = `${rect.top + window.scrollY}px`;

    // Mostrar el input
    inputField.value = matchText.textContent;
    inputField.style.display = 'block';
    inputField.focus();

    // Actualizar texto
    inputField.onblur = () => putPuntuationValue(inputField, matchText, matchGroup);
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
        playerToNextMatch(puntaje1, puntaje2, parentGroup);
    }
}

// Funcion que maneja la logica cuando ya se introdujeron los dos puntajes de los players y uno debe de pasar a la siguente ronda
function playerToNextMatch(puntaje1, puntaje2, parentGroup) {
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
    nextPlayerPlace.classList.add('changed');
}

// Devuelve el elemento text del DOM que tenga el idToSearch como player
function findPlayerInOtherMatch(idToSearch) {
    const matchups = svg.querySelectorAll(".matchup");
    let result;
    for (let i = 0; i < matchups.length; i++) {
        const element = matchups[i];
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
    svg.querySelectorAll(".matchup__player1").forEach((element) => element.classList.remove('winner','loser'));
    svg.querySelectorAll(".matchup__player2").forEach((element) => element.classList.remove('winner','loser'));
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