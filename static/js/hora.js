document.addEventListener("DOMContentLoaded", function () {
    flatpickr("#hora", {
        enableTime: true,       // Habilitar selector de hora
        noCalendar: true,       // Deshabilitar el calendario
        dateFormat: "H:i",      // Formato 24 horas (usa "h:i K" para 12 horas con AM/PM)
        time_24hr: true,        // Activar formato de 24 horas
        minuteIncrement: 5      // Incrementos de 5 minutos
    });
});