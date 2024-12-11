document.addEventListener("DOMContentLoaded", function () {
    const horaInput = document.getElementById("hora");

    // Configuración de flatpickr
    const picker = flatpickr("#hora", {
        enableTime: true,       // Habilitar selector de hora
        noCalendar: true,       // Deshabilitar el calendario
        dateFormat: "H:i",      // Formato 24 horas
        time_24hr: true,        // Activar formato de 24 horas
        minuteIncrement: 5,     // Incrementos de 5 minutos
        minTime: "18:00",       // Hora mínima
        maxTime: "23:00",       // Hora máxima
        defaultDate: "18:00"    // Hora preseleccionada en el reloj
    });

    // Verificar si el campo se llena automáticamente y reiniciarlo
    if (horaInput.value) {
        horaInput.value = ""; // Resetea el valor del campo si se llena automáticamente
    }
});
