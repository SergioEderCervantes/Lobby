// ------------------------------------ Miscelaneos ------------------------------------


// Cambiar la url para que la redirija al change
const change_link = document.getElementById('change_info')
if (change_link){
    const current_url = change_link.href;
    console.log(current_url);
    const new_url = current_url.replace("/view/#", "/change");
    console.log(new_url);
    change_link.href = new_url;
}

// ------------------------------------Parte que maneja los eventos de Drag------------------------------------
document.getElementById('svg_enfrentamientos').addEventListener('load', function(){
    const draw = SVG('#svg_enfrentamientos')
    draw.find('.matchup__player').forEach(element => {
        element.draggable();
        // Opcional: Añadir eventos para monitorear el arrastre
        element.on('dragstart', function (event) {
            console.log('Inicio de arrastre:', event.detail.p.x, event.detail.p.y);
        });
    
        element.on('dragmove', function (event) {
            console.log('Arrastrando:', event.detail.p.x, event.detail.p.y);
        });
    
        element.on('dragend', function (event) {
            console.log('Fin de arrastre:', event.detail.p.x, event.detail.p.y);
        });
    })
    
});

// ------------------------------------Parte que maneja los eventos de Puntuacion------------------------------------
// --------------------------Parte que Maneja el Boton de guardar si hubo modificaciones al svg----------------


// ------------------------------------Parte que manda el SVG de vuelta al server------------------------------

// Funcion que manda el svg al servidor, se llama cuando ocurre una modificacion en el svg, sobretodo el cambio de jugadores
// Espera una instancia de SVG.js, el csrf_token y el id del torneo
async function send_SVG(draw, csrf_token, torneo_id) {
    const svgElement = draw.node;
    const svgData = svgElement.outerHTML;

   
    try {
        // TODO cambiar la url a la direccion del back que va a procesar esto
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
        }else{
            
            console.log("Hubo un problema al enviar el SVG.");
        }
        
    }
    catch (error){
        console.error("Error en la solicitud:", error);
    }
}