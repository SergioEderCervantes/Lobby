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
function openPopup({ title, svg, message, buttonText, size = 'small', imageUrl = null, torneoUrl = "", onEvent = null}) {
    const overlay = document.getElementById('popup_overlay');
    const container = document.getElementById('popup_container');
    const content = document.getElementById('popup_content');

    // Ajustar tamaño del popup
    container.className = `popup_container ${size}`;

    // Configurar contenido dinámico
    let dynamicContent = `
        <h2>${title}</h2>
    `;

    if (size === 'large' && imageUrl) {
        dynamicContent += `<img id="popup_image" src="${imageUrl}" alt="Imagen del popup" />`;
    } else if (size === 'small' && svg) {
        dynamicContent += `<div class="popup_svg">${svg}</div>`;
    } else if (size === 'medium') {
        dynamicContent += ''; // En "medium", solo se muestra título y mensaje
    }

    dynamicContent += `
        <p>${message}</p>
    `;

    if (size === 'large') {
        dynamicContent += `<a href="${torneoUrl}" class="popup_button" target="_blank">${buttonText}</a>`;
    } else {
        dynamicContent += `<button class="popup_button" onclick="handlePopupAction('${size}', ${onEvent ? 'true' : 'false'})">${buttonText}</button>`;
    }

    // Insertar contenido dinámico
    content.innerHTML = dynamicContent;
    
    // Ocultar loader y mostrar popup
    hideLoader();
    container.classList.remove('hidden');
    overlay.classList.remove('hidden');

    // Cerrar el popup al hacer clic fuera del contenedor
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            closePopup(size);
        }
    });
}

// Manejar la acción del botón del popup
function handlePopupAction(size, hasEvent) {
    closePopup(size);
    if (hasEvent && typeof register_reservation === 'function') {
        showLoader();
        register_reservation();
    }
}


// Función para cerrar el popup
function closePopup(size = 'small') {
    const overlay = document.getElementById('popup_overlay');
    const container = document.getElementById('popup_container');

    container.classList.add('hidden');
    setTimeout(() => {
        if (size !== 'medium'){
            overlay.classList.add('hidden');
        }
        if (size === 'small'){
            location.reload();
         }
    }, 50);
}
