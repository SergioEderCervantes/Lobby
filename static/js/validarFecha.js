document.addEventListener("DOMContentLoaded", () => {
    const inputFecha = document.getElementById("fecha");
    inputFecha.addEventListener("change", checarDisp);
});

async function checarDisp() {
    limpiarCampos();
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
            throw new Error(JSON.stringify(errorData));
        }
        
        const data = await response.json();
        console.log("Disponibilidad:", data.disponibilidad);
        actualizarBotones(data.disponibilidad);
    } catch (error) {
        let errorData;
        try{
            errorData = JSON.parse(error.message)
        } catch{
            errorData = { message: error.message}
        }
        console.error("Error capturado:", errorData.error);
        openPopup({
            title: "Error",
            svg: errorSVG,
            message: errorData.error || "Error desconocido",
            buttonText: "Aceptar",
            size: 'small'
        })
    }
}

function limpiarCampos(){
    document.querySelectorAll(".campoForm").forEach((campo) =>{
        campo.classList.remove("visible");
        input = campo.querySelector('input');
        input ? input.classList.remove("visible")
        : limpiarFormatoCampo(campo);
    })
    //Hacer visible el primero
    document.querySelector(".campoForm").classList.add("visible");
    //Deshabilitar el boton
    document.getElementById("register_reservation").disabled = true;

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
    reestablecerBotones();
}

function reestablecerBotones(){
    const botones = document.querySelectorAll(".consola-button");

    botones.forEach(boton => {
        const consola = boton.getAttribute("data-consola");
            boton.disabled = false; // Habilitar el botón
            boton.style.backgroundColor = ""; // Restaurar color original
            boton.style.borderColor = "";
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

        if (disponibilidad[consola]) {
            boton.disabled = false; // Habilitar el botón
            boton.classList.remove("disabled"); // Remover la clase de deshabilitado
        } else {
            boton.disabled = true; // Deshabilitar el botón
            boton.classList.add("disabled"); // Agregar la clase de deshabilitado
        }
    });
}
