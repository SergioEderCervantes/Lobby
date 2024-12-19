document.addEventListener("DOMContentLoaded", () => {
    // Manejo del evento de inscripcion
    const registerButton = document.getElementById("tournament_register_btn");
    const submitGuestButton = document.getElementById("guest_register_form");
    if (registerButton) {
        registerButton.addEventListener("click", register_player);
    }
    if (submitGuestButton) {
        submitGuestButton.addEventListener("submit", register_gest_player)
    }

});
const errorSVG = `<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                    viewBox="0 0 50 50" xml:space="preserve">
                    <circle style="fill:#D75A4A;" cx="25" cy="25" r="25"/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,34 25,25 34,16 
                    "/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,16 25,25 34,34 
                    "/>
                    </svg>`;

const success_svg = `<svg width="200px" height="200px" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><defs><style>
                    .cls-1 {
                        fill: #699f4c;
                        fill-rule: evenodd;
                    }
                </style>
                </defs>
                <path class="cls-1" d="M800,510a30,30,0,1,1,30-30A30,30,0,0,1,800,510Zm-16.986-23.235a3.484,3.484,0,0,1,0-4.9l1.766-1.756a3.185,3.185,0,0,1,4.574.051l3.12,3.237a1.592,1.592,0,0,0,2.311,0l15.9-16.39a3.187,3.187,0,0,1,4.6-.027L817,468.714a3.482,3.482,0,0,1,0,4.846l-21.109,21.451a3.185,3.185,0,0,1-4.552.03Z" id="check" transform="translate(-770 -450)"/>
                </svg>`; 

async function register_player() {
    showLoader();

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
            throw new Error(JSON.stringify(errorData));
        }

        const data = await response.json();
        openPopup({
            title: "Inscripcion exitosa",
            svg: success_svg,
            message: data.message || "Operacion exitosa",
            buttonText: "Aceptar",
            size: 'small'
        });
    } catch (error) {
        let errorData;
        try{
            errorData = JSON.parse(error.message);
        } catch {
            errorData = { message: error.message}
        }

        openPopup({
            title: "Error en la inscripcion",
            svg: errorSVG,
            message: error.message || "Error desconocido",
            buttonText: "Aceptar",
            size: 'small'
        });
    }
}

async function register_gest_player(event) {
    event.preventDefault();
    showLoader();


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
            throw new Error(JSON.stringify(errorData)); // Lanzar el error con los datos del JSON
        }

        const data = await response.json(); // Parsear la respuesta JSON
        console.log("Respuesta JSON:", data);
        openPopup({
            title: "Inscripcion exitosa",
            svg: success_svg,
            message: data.message || "Operacion exitosa",
            buttonText: "Aceptar",
            size: 'small'
        });

    } catch (error) {
        console.error("Error capturado:", error);

        // Intentar parsear el JSON del error lanzado
        let errorData;
        try {
            errorData = JSON.parse(error.message); // Intentar extraer el JSON
        } catch {
            errorData = { message: error.message}; // Fallback
        }
    
        openPopup({
            title: "Error en la inscripcion",
            svg: errorSVG,
            message: error.error || "Error desconocido",
            buttonText: "Aceptar",
            size: 'small'
        });
    }
}

