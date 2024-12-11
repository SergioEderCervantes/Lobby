document.addEventListener("DOMContentLoaded", () => {
    const inputFecha = document.getElementById("fecha");
    inputFecha.addEventListener("change", checarDisp);
});

async function checarDisp() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Obtiene el token CSRF del DOM
    const sucursalId = 1; // ID de la sucursal, puedes cambiarlo dinámicamente si es necesario
    const fecha = document.getElementById("fecha").value; // Obtiene el valor del campo de fecha

    try {
        const response = await fetch('/reservations/check_availability/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // CSRF token necesario para solicitudes POST
            },
            body: JSON.stringify({
                fecha: fecha,
                sucursal_id: sucursalId
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error("Error:", errorData.error);
            //alert(`Error: ${errorData.error}`); // Usar backticks para interpolación
            mostrarError(errorData.error);
            return;
           
        }

        const data = await response.json();
        actualizarBotones(data.disponibilidad);
        //console.log("Disponibilidad:", data.disponibilidad);
        //alert(`Disponibilidad: ${JSON.stringify(data.disponibilidad)}`); // Mostrar disponibilidad
    } catch (error) {
        //console.error("Error inesperado:", error);
        //alert(`Error inesperado: ${error.message}`);
    }
}

function mostrarError(mensaje) {
    // Muestra una ventana modal con el error
    const modal = document.getElementById("error-modal");
    const modalMessage = document.getElementById("modal-mensaje");
    const form = document.getElementById("reservation-form");
    const fields = form.querySelectorAll(".campoForm");
    const toggleSwitch = document.querySelector('.toggle-input'); // Obtener el interruptor de términos y condiciones
    const termsContainer = document.querySelector('.terms-container'); // Obtener el contenedor de términos
    const botonReservar = document.getElementById("register_reservation"); // Obtener el botón de reserva
    
    const inputFecha = document.getElementById("fecha");
    inputFecha.value = ""; // Resetea el valor del campo de fecha

    // Resetea los campos del formulario y oculta los que corresponden
    fields.forEach((field, index) => {
        if (index > 0) {
            field.classList.remove("visible"); // Elimina la clase 'visible' para hacer el campo invisible
        }
        const input = field.querySelector("input, textarea");
        if (input) {
            input.value = ""; // Resetea el valor del campo
        }
    });

    // Desactivar el toggle de términos y condiciones
    toggleSwitch.disabled = true;
    toggleSwitch.style.opacity = '0.5'; // Transparente

    // Deshabilitar el contenedor de términos
    termsContainer.style.opacity = '0.5'; // Transparente
    termsContainer.style.pointerEvents = 'none'; // Desactiva la interactividad
    
    botonReservar.disabled = true;
    botonReservar.style.opacity = '0.5'; // Transparente
    botonReservar.style.cursor = 'not-allowed'; // Cursor no permitido

    // Llamada para reestablecer botones
    reestablecerBotones();

    // Configura el mensaje y muestra el modal
    modalMessage.textContent = mensaje;
    modal.style.display = "block";

    // Configura el botón para cerrar el modal
    const closeButton = document.getElementById("close-modal");
    closeButton.addEventListener("click", () => {
        modal.style.display = "none";
    });
    
}


function formatearCampoError(campo) {
    // Agregar un estilo de error al campo
    campo.style.borderColor = "red";
    campo.style.backgroundColor = "#ffe6e6"; // Fondo rojo claro
    campo.focus(); // Enfocar el campo para que el usuario lo corrija
}

function limpiarFormatoCampo(campo) {
    // Restaurar el formato original del campo
    campo.style.borderColor = "";
    campo.style.backgroundColor = "";
}

function reestablecerBotones(){
    const botones = document.querySelectorAll(".consola-button");

    botones.forEach(boton => {
        const consola = boton.getAttribute("data-consola");
            boton.disabled = false; // Habilitar el botón
            boton.style.backgroundColor = ""; // Restaurar color original
            boton.style.cursor = "pointer"; // Restaurar cursor
            boton.classList.remove("disabled", "no-hover"); // Remover clases
            boton.style.transform = ""; // Restaurar transformación al hover
            boton.style.transition = ""; // Restaurar transición
            boton.style.border = "";
    });
}

function actualizarBotones(disponibilidad) {
    const botones = document.querySelectorAll(".consola-button");

    botones.forEach(boton => {
        const consola = boton.getAttribute("data-consola");


        // Verifica la disponibilidad
        if (disponibilidad[consola]) {
            boton.disabled = false; // Habilitar el botón
            boton.style.backgroundColor = ""; // Restaurar color original
            boton.style.cursor = "pointer"; // Restaurar cursor
            boton.classList.remove("disabled", "no-hover"); // Remover clases
            boton.style.transform = ""; // Restaurar transformación al hover
            boton.style.transition = ""; // Restaurar transición
        } else {
            boton.disabled = true; // Deshabilitar el botón
            boton.style.backgroundColor = "rgba(255, 0, 0, 0.1)"; // Cambiar color a rojo claro
            boton.style.cursor = "not-allowed"; // Cambiar cursor a "no permitido"
            boton.style.transform = "none"; // Desactivar transformación al hover
            boton.style.transition = "none"; // Desactivar transición al hover
        }
    });
}
