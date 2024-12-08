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

    document.getElementById("tournament_register_btn").addEventListener("click", register_player);

});


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
            openPopup({
                title: "Error en la inscripcion",
                svg: `<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                    viewBox="0 0 50 50" xml:space="preserve">
                    <circle style="fill:#D75A4A;" cx="25" cy="25" r="25"/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,34 25,25 34,16 
                    "/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,16 25,25 34,34 
                    "/>
                    </svg>`,
                message: errorData.message || "Error desconocido",
                buttonText: "Aceptar",
                size: 'small'
            });
            return;
        }
        
        const data = await response.json();
        openPopup({
            title: "Inscripcion exitosa",
            svg: `<svg width="200px" height="200px" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><defs><style>
                    .cls-1 {
                        fill: #699f4c;
                        fill-rule: evenodd;
                    }
                </style>
                </defs>
                <path class="cls-1" d="M800,510a30,30,0,1,1,30-30A30,30,0,0,1,800,510Zm-16.986-23.235a3.484,3.484,0,0,1,0-4.9l1.766-1.756a3.185,3.185,0,0,1,4.574.051l3.12,3.237a1.592,1.592,0,0,0,2.311,0l15.9-16.39a3.187,3.187,0,0,1,4.6-.027L817,468.714a3.482,3.482,0,0,1,0,4.846l-21.109,21.451a3.185,3.185,0,0,1-4.552.03Z" id="check" transform="translate(-770 -450)"/>
                </svg>`,
            message: data.message || "Operacion exitosa",
            buttonText: "Aceptar",
            size: 'small'
        });
    } catch (error) {
        openPopup({
            title: "Error en la inscripcion",
            svg: `<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                    viewBox="0 0 50 50" xml:space="preserve">
                    <circle style="fill:#D75A4A;" cx="25" cy="25" r="25"/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,34 25,25 34,16 
                    "/>
                    <polyline style="fill:none;stroke:#FFFFFF;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;" points="16,16 25,25 34,34 
                    "/>
                    </svg>`,
            message: error.message || "Error desconocido",
            buttonText: "Aceptar",
            size: 'small'
        });
    }
}

