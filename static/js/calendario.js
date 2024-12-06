document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#fecha", {
        enableTime: false, // Deshabilitar selector de hora
        dateFormat: "Y-m-d", // Formato de fecha
        minDate: "today", // Fecha mínima permitida
        locale: "es", // Idioma en español
    });
});
