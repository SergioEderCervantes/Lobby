document.addEventListener('DOMContentLoaded', () => {
    // Selecciona todas las tarjetas de torneo
    const tournamentCards = document.querySelectorAll('.tournament_card');
    
    // Verifica si solo hay un torneo
    if (tournamentCards.length <= 1 ) {
        // Selecciona todos los elementos SVG o imágenes con clase 'icons-over' y similares
        const icons = document.querySelectorAll('.icons-over1, .icons-over3, .icons-over4, .icons-over5');
        
        // Itera sobre cada ícono y establece width y height en 0
        icons.forEach(icon => {
            icon.style.width = '0';
            icon.style.height = '0';
        });
    }
    else{
        if(tournamentCards.length == 3){
            // Selecciona todos los elementos SVG o imágenes con clase 'icons-over' y similares
            const icons = document.querySelectorAll('.icons-over1, .icons-over4');
            
            // Itera sobre cada ícono y establece width y height en 0
            icons.forEach(icon => {
                icon.style.width = '0';
                icon.style.height = '0';
            });
        }
    }
});
