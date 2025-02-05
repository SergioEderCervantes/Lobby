document.addEventListener("DOMContentLoaded", () => {
    // Manejo del evento de inscripcion
    const registerButton = document.getElementById("tournament_register_btn");
    const guestForm = document.getElementById("guest_register_form");
    if (registerButton) {
        registerButton.addEventListener("click", register_player);
    }
    if (guestForm) {
        guestForm.addEventListener("submit", register_gest_player)
    }

});

async function register_player() {
    const popup = new Popup();

    try {
        const response = await fetch("/tournaments/register_player/", {
            method: "POST",
            headers: {
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
            throw new Error(errorData.error);
        }
        await popup.ejec({
            title: "Inscripcion Exitosa",
            icon: "success",
            text: "Usuario registrado al torneo con exito",
        });
    } catch (error) {
        await popup.ejec({
            title: "Error en la inscripcion",
            icon: "error",
            text: error.message || "Error desconocido",
        });
    } finally {
        popup.closeOverlay();
        location.reload();
    }
}

async function register_gest_player(event) {
    event.preventDefault();
    const popup = new Popup();
    const form = event.target;
    const url = form.action;
    const formData = new FormData(form);

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
            title: "Inscripcion exitosa",
            icon: "success",
            text: "Usuario registrado con Exito",
        });
    } catch (error) {
        await popup.ejec({
            title: "Error en la inscripcion",
            icon: "error",
            text: error.message || "Error desconocido",
        });
    } finally {
        popup.closeOverlay();
        location.reload();
    }
}

