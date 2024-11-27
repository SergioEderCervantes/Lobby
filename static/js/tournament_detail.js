document.addEventListener("DOMContentLoaded", () => {
    const dropdown = document.querySelector(".dropdown");
    const dropdown_button = document.getElementById("dropdown-btn");
    const dropdown_menu = document.getElementById("dropdown-menu");
    
    dropdown_button.addEventListener("click", () => {
        const currentWidth = dropdown.offsetWidth; // Obtener el ancho actual
        const currentHeight = dropdown.offsetHeight // Alto actual
        const liCant = dropdown_menu.querySelectorAll("li").length;
        // Si no está expandido, expandimos
        if (!dropdown.classList.contains("expanded")) {
            dropdown_button.textContent = "Ocultar jugadores inscritos"
            
            const targetWidth = 300; // Ancho al que queremos expandir
            const targetHeight = liCant * 38 + dropdown_button.offsetHeight + 50; // Alto a expandir
            // Crear animación para expandir
            createAnimation("expandWidth", currentWidth, targetWidth, currentHeight, targetHeight);
            dropdown.classList.remove("collapsing"); // Asegurarnos de que no esté colapsando
            dropdown.classList.add("expanded");
        } else {
            dropdown_button.textContent = "Mostrar jugadores inscritos"

            const targetWidth = dropdown_button.offsetWidth; // Ancho al que queremos colapsar
            const targetHeight = dropdown_button.offsetHeight ; // Alto a colapsar
            // Si está expandido, lo colapsamos
            createAnimation("collapseWidth", currentWidth, targetWidth, currentHeight, targetHeight); // Animación para regresar al estado original
            dropdown.classList.remove("expanded");
            dropdown.classList.add("collapsing");
        }

        //Toggle de los otros dos elementos:
        dropdown_button.classList.toggle("expanded");
        dropdown_menu.classList.toggle("expanded");
    });

    /**
     * Crea una regla de animación dinámica
     * @param {string} name - Nombre de la animación
     * @param {number|string} fromWidth - Ancho inicial
     * @param {number|string} toWidth - Ancho final
     * @param {number|string} fromHeight - Alto inicial
     * @param {number|string} toHeight - Alto final
     */
    function createAnimation(name, fromWidth, toWidth, fromHeight, toHeight) {
        // Buscar la hoja de estilo específica
        const styleSheet = Array.from(document.styleSheets).find(sheet =>
            sheet.href && sheet.href.includes("tournament_detail.css")
        );
        if(!styleSheet){
            console.log("NO ENCONTRO LA STYLESHEET");
            return;
        }

        // Eliminar reglas existentes con el mismo nombre
        for (let i = styleSheet.cssRules.length - 1; i >= 0; i--) {
            if (styleSheet.cssRules[i].name === name) {
                styleSheet.deleteRule(i);
            }
        }

        // Definir la nueva animación
        const keyframes = `
            @keyframes ${name} {
                from {
                    width: ${fromWidth}px;
                    height: ${fromHeight}px;
                    
                }
                to {
                    width: ${toWidth}px;
                    height: ${toHeight}px;
                }
            }
        `;
        styleSheet.insertRule(keyframes, styleSheet.cssRules.length);
    }
});

