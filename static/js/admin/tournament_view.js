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

// ------------------------------------Parte que maneja los eventos de Drag------------------------------------
const nodes = [];
document.getElementById('svg_enfrentamientos').addEventListener('load', function () {
    const draw = SVG('#svg_enfrentamientos')

    draw.find('.matchup__player').forEach(element => {
        nodes.push(element.node);


        element.draggable();
        // Opcional: Añadir eventos para monitorear el arrastre
        element.on('dragstart', (event) => dragstart(event, element));

        element.on('dragmove', function (event) {
            // console.log('Arrastrando:', event.detail.p.x, event.detail.p.y);
        });

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
        // Que el boton de guardar aparezca
        const button = document.getElementById('send__button');
        button.classList.remove('hide');
    }

    //Regresar el elemento a su posicion original
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

// ------------------------------------Parte que maneja los eventos de Puntuacion------------------------------------

document.querySelectorAll(".match__puntaje__player1").forEach((rect) =>{
    rect.addEventListener('click',(event) => activateInput(event.target, 1))
});
document.querySelectorAll(".match__puntaje__player2").forEach((rect) =>{
    rect.addEventListener('click',(event) => activateInput(event.target, 2))
});

function activateInput(target, playerNum){
    const inputField = document.getElementById("svg_input")
    const matchGroup = target.closest('g');
    const className = playerNum == 1 ? ".match__puntaje__player1__text" : ".match__puntaje__player2__text";
    const matchText = matchGroup.querySelector(className);
    const parentGroup = target.closest('g');
    const matchId = parentGroup.id;

    // Pocisionar el input en donde se dio el click
    const rect = target.getBoundingClientRect();
    console.log(rect);
    inputField.style.left = `${rect.left + window.scrollX + 0.5}px`;
    inputField.style.top = `${rect.top + window.scrollY + 1}px`;

    // Mostrar el input
    inputField.value = matchText.textContent;
    inputField.style.display = 'block';
    inputField.focus();

    // Actualizar texto
    inputField.onblur = () => updateSVGText(inputField, matchText);
    inputField.onkeyup = (e) => {
        if (e.key === 'Enter'){
            e.preventDefault(); // Asegurarnos de que no haya un comportamiento no deseado con Enter
            updateSVGText(inputField, matchText);
        }

    } 
}

function updateSVGText(inputField, matchText){
    
    if ( inputField.value === ""){
        return;
    }
    matchText.textContent = inputField.value;
    inputField.value = "";
    inputField.style.display = "none";
}


// --------------------------Parte que Maneja el Boton de guardar si hubo modificaciones al svg----------------


document.getElementById('send__button').addEventListener('click', function () {
    const draw = SVG('#svg_enfrentamientos');
    send_SVG(draw,csrfToken,tournamentId);
    this.classList.add('hide')
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