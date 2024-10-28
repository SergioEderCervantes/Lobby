// ------------------------------------Parte que crea el SVG con toda la data------------------------------------



if(!matchups_ready){
    const width = 1200;
    const height = 800;
    const draw = SVG().addTo(".matches__list").size(width, height);
    const rect_group = draw.group();
    // Número de niveles de la estructura del torneo
    const levels = is_ideal ? Math.log2(enfrentamientos.length)+1 : Math.floor(Math.log2(enfrentamientos.length)); 
    // Distancia horizontal entre niveles
    const xOffset = 250;
    // Distancia vertical base
    const yOffset = 100;
    // Factor de escalado de yOffset en cada nivel 
    const scale = 2; 
    
    const connector_points= [];
    
    let cx = 250;
    for (let level = 0; level < levels; level++) {
        connector_points[level] = [];
        let cy = yOffset * Math.pow(scale, level) / 2;
        const matchesInLevel = enfrentamientos.length / Math.pow(2, level);
    
        for (let i = 0; i < matchesInLevel; i++) {
            const matchData = level === 0 ? enfrentamientos[i] : { id: "", player1: "", player2: "" };
            connector_points[level][i] = create_match_square(draw, matchData.id, matchData.player1, matchData.player2, cx, cy);
            cy += yOffset * Math.pow(scale, level);
        }
        cx += xOffset; // Avanza horizontalmente al siguiente nivel
    }
    const lines_group = draw.group();
    
    for (let i = 0; i < connector_points.length; i++) {
        if (i + 1 != connector_points.length){
            connect_levels(draw,lines_group,true,connector_points[i],connector_points[i+1])
        }
    }
    
    // Con el svg terminado, falta mandarlo al back
    
    const sent = send_SVG(draw, csrf_token, torneo_id);   
}



function create_match_square(draw, match_id, player1, player2, cx, cy) {
    const width = 200;
    const height = 50;
    const padding = 12;
    const x = cx + 0.5*(padding-width);
    const y = cy+0.5*(padding-height);
    const outer = draw.rect(width, height).attr({ fill: 'black' }).center(cx, cy);
    const inner = draw.rect(width - padding, height - padding).attr({ fill: 'white' }).center(cx, cy);
    const group_info = draw.group().center(cx, cy);
    group_info.text(player1).move(x , y).font({ size: 14, fill: 'black' });
    group_info.text(player2).move(x, y + 20).font({ size: 14, fill: 'black' });
    group_info.text(match_id).center(x - 20, cy).font({size: 14, fill: 'white'});
    return outer;
}

function connect_levels(draw,group, isIdeal, level1, level2){
    let pivot = 0;
    if (isIdeal){
        level2.forEach(match =>{
            let point1 = [level1[pivot].cx() + 100, level1[pivot].cy()];
            let point2 = [level1[pivot+1].cx() + 100, level1[pivot+1].cy()];
            let center_point = [match.cx() - 100,match.cy()];
            group.add(draw.polyline([point1, center_point]).fill('none').stroke({ width: 2, color: 'white' }));
            pivot +=2;
            group.add(draw.polyline([point2,center_point]).fill('none').stroke({ width: 2, color: 'white'}));
        })
    }
}
// ------------------------------------Parte que maneja los eventos de Drag------------------------------------



// --------------------------Parte que Maneja el Boton de guardar si hubo modificaciones al svg----------------


// ------------------------------------Parte que manda el SVG de vuelta al server------------------------------

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