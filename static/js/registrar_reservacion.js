document.addEventListener("DOMContentLoaded", () => {
    const submit_btn = document.getElementById("reservation-form")
    submit_btn.addEventListener("submit", showConfirmation);
});

function showConfirmation(event) {
    event.preventDefault();
    
    const popup = new Popup();
    popup.closeLoader();


    const form = event.target;
    const formData = new FormData(form);

    let dataDisplay = "Fecha: \nHora: \nNum_personas: ";

    for (const [key, value] of formData.entries()) {
        switch (key) {
            case 'fecha':
                dataDisplay = dataDisplay.replace("Fecha: ", `Fecha: ${value}`);
                break;
            case 'hora':
                dataDisplay = dataDisplay.replace("Hora: ", `Hora: ${value}`);
                break;
            case 'num_personas':
                dataDisplay = dataDisplay.replace("Num_personas: ", `# Personas: ${value} `);
                break;
        }
    }

    popup.ejec({
        title: "Confirmar Reservacion",
        icon: "question",
        text: dataDisplay,
        showCancelButton: true,
    }).then((result) => {
        if (result.isConfirmed) {
            popup.closeOverlay();
            register_reservation();
        }
        else{
            location.reload();
        }
    });
}
async function register_reservation() {
    const popup = new Popup();

    const form = document.getElementById("reservation-form");
    const url = form.action;
    const formData = new FormData(form);
    const consolas_container = document.getElementById("consolas-buttons");

    // Obtener el botón con la clase "seleccionado"
    const selectedButton = consolas_container.querySelector('.consola-button.seleccionado');
    if (selectedButton) {
        // Recuperar el valor de data-consola
        const consola = selectedButton.getAttribute('data-consola');

        // Añadir el valor de consola al formData
        formData.append('consola_name', consola);
    } else {
        console.error('No se ha seleccionado ninguna consola');
        return; // Detener la ejecución si no hay selección
    }

    try {
        // Realizar la solicitud fetch al backend
        const response = await fetch(url, {
            method: form.method,
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken') || ''
            }
        });

        if (!response.ok) {
            const errorData = await response.json(); // Extraer el JSON del error
            throw new Error(errorData.error); // Lanzar el error con los datos del JSON
        }

        await popup.ejec({
            title: "Reservacion completada con exito",
            icon: "success",
            text: "La reservacion fue registrada correctamente",
        });

    } catch (error) {
        await popup.ejec({
            title: "Error en la reservacion",
            icon: "error",
            text: error.message || "Error desconocido"
        });
    } finally {
        location.reload();
    }
}