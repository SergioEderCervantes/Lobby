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
            alert(`Error: ${errorData.error}`); // Usar backticks para interpolación
            return;
        }

        const data = await response.json();
        console.log("Disponibilidad:", data.disponibilidad);
        alert(`Disponibilidad: ${JSON.stringify(data.disponibilidad)}`); // Mostrar disponibilidad
    } catch (error) {
        console.error("Error inesperado:", error);
        alert(`Error inesperado: ${error.message}`);
    }
}

function mostrarError(mensaje) {
    // Muestra una ventana modal con el error
    const modal = document.getElementById("error-modal");
    const modalMessage = document.getElementById("modal-mensaje");

    modalMessage.textContent = mensaje;
    modal.style.display = "block";

    // Cierra la ventana modal al hacer clic en el botón
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