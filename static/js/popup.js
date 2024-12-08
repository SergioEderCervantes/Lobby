// Función para mostrar el loader
function showLoader() {
    const overlay = document.getElementById('popup_overlay');
    const loader = document.getElementById('popup_loader');

    overlay.classList.remove('hidden'); // Mostrar overlay
    loader.classList.remove('hidden'); // Mostrar loader
}

// Función para ocultar el loader
function hideLoader() {
    const loader = document.getElementById('popup_loader');
    loader.classList.add('hidden'); // Ocultar loader
}

// Función para abrir el popup (después de que termine el loader)
function openPopup({ title, svg, message, buttonText, size = 'large', imageUrl = null, torneoUrl = ""}) {
    const overlay = document.getElementById('popup_overlay');
    const container = document.getElementById('popup_container');
    const content = document.getElementById('popup_content');
    const image = document.getElementById('popup_image'); // Imagen renderizada por Django

    // Ajustar tamaño del popup
    container.className = `popup_container ${size}`;

// Configurar contenido dinámico
const dynamicContent = `
    <h2>${title}</h2>
    ${
        size === 'large' && imageUrl
            ? `<img id="popup_image" src="${imageUrl}" alt="Imagen del popup" />`
            : svg
            ? `<div class="popup_svg">${svg}</div>`
            : ''
    }
    <p>${message}</p>
    ${
        size === 'large'
            ? `<a class="popup_button" href="${torneoUrl}" style="text-decoration: none;">${buttonText}</a>`
            : `<button class="popup_button" onclick="closePopup()">${buttonText}</button>`
    }
`;


    // Insertar contenido dinámico
    content.innerHTML = dynamicContent;
    // Ocultar loader y mostrar popup
    hideLoader();
    container.classList.remove('hidden');
    overlay.classList.remove('hidden');
    // Cerrar el popup al hacer clic fuera del contenedor
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            closePopup();
        }
    });
}

// Función para cerrar el popup
function closePopup() {
    const overlay = document.getElementById('popup_overlay');
    const container = document.getElementById('popup_container');

    container.classList.add('hidden');
    setTimeout(() => {
        overlay.classList.add('hidden');
    }, 50);
}
