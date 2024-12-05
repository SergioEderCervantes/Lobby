document.addEventListener("DOMContentLoaded", () => {
    const accordionHeaders = document.querySelectorAll(".accordion_header");

    accordionHeaders.forEach(header => {
        header.addEventListener("click", () => {
            const content = header.nextElementSibling;
            // const item = header.parentElement;
            // Cerrar todos los contenidos excepto el actual
            document.querySelectorAll(".accordion_content").forEach(otherContent => {
                if (otherContent !== content) {
                    otherContent.classList.remove("open");
                    otherContent.previousElementSibling.classList.remove("active"); // Quitar clase activa de los headers
                }
            });

            // Alternar la visibilidad del contenido actual
            content.classList.toggle("open");
            header.classList.toggle("active"); // Cambiar el estado del ícono
        });
    });
    
    // Manejo del evento de inscripcion

    document.getElementById("tournament_register_btn").addEventListener("click",register_player);

});
    

async function register_player() {
    try{
        const response = await fetch("/tournaments/register_player/",{
            method: "POST",
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                usuario_id: userId,
                torneo_id: tournamentId,
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            mostrarPopup(`Error: ${errorData.error || "Error desconocido"}`);
            return;
        }

        const data = await response.json();
        mostrarPopup(`Éxito: ${data.message || "Operación exitosa"}`);
    } catch (error) {
        mostrarPopup(`Error inesperado: ${error.message || "Error desconocido"}`);
    }
}

// Función para mostrar el popup
function mostrarPopup(mensaje) {
    // Crear el contenedor del popup
    const popup = document.createElement('div');
    popup.style.position = 'fixed';
    popup.style.top = '50%';
    popup.style.left = '50%';
    popup.style.transform = 'translate(-50%, -50%)';
    popup.style.backgroundColor = '#fff';
    popup.style.padding = '20px';
    popup.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    popup.style.borderRadius = '8px';
    popup.style.zIndex = '1000';
    popup.style.textAlign = 'center';
    popup.style.color = 'black';

    // Crear el mensaje dentro del popup
    const mensajeTexto = document.createElement('p');
    mensajeTexto.textContent = mensaje;
    popup.appendChild(mensajeTexto);

    // Crear el botón de aceptar
    const botonAceptar = document.createElement('button');
    botonAceptar.textContent = 'Aceptar';
    botonAceptar.style.marginTop = '10px';
    botonAceptar.style.padding = '10px 20px';
    botonAceptar.style.border = 'none';
    botonAceptar.style.backgroundColor = '#007BFF';
    botonAceptar.style.color = '#fff';
    botonAceptar.style.borderRadius = '4px';
    botonAceptar.style.cursor = 'pointer';

    // Agregar el evento para ocultar el popup al hacer clic
    botonAceptar.addEventListener('click', () => {
        document.body.removeChild(popup);
    });

    popup.appendChild(botonAceptar);
    document.body.appendChild(popup);
}
