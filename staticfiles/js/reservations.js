document.getElementById('reservation-form').onsubmit = function (event) {
    event.preventDefault(); // Evita que el formulario se envíe

    // Obtener los datos del formulario
    const nombre = document.getElementById('nombre') ? document.getElementById('nombre').value : "Usuario";
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;
    const numPersonas = document.getElementById('num_personas').value;
    const comentarios = document.getElementById('comentarios').value || "Sin comentarios";

    // Mostrar los detalles en el modal
    const detalles = `
        <strong>Nombre:</strong> ${nombre}<br>
        <strong>Fecha:</strong> ${fecha}<br>
        <strong>Hora:</strong> ${hora}<br>
        <strong>Número de personas:</strong> ${numPersonas}<br>
        <strong>Comentarios:</strong> ${comentarios}
    `;
    document.getElementById('modal-detalles').innerHTML = detalles;

    // Mostrar el modal
    const modal = document.getElementById('reservation-modal');
    modal.style.display = 'flex';

    // Limpiar el formulario después de mostrar el modal
    document.getElementById('reservation-form').reset();

    // Manejar el cierre del modal con el botón
    const closeButton = document.getElementById('close-modal');
    closeButton.onclick = function () {
        modal.style.display = 'none';
    };

    // Cerrar al hacer clic fuera del modal
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
};
