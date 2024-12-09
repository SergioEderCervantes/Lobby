document.querySelectorAll('.consola-button').forEach((boton, index) => {
    const form = document.getElementById("reservation-form");
    const fields = form.querySelectorAll(".campoForm");
    const botonReservar = document.getElementById("register_reservation"); // Obtener el botón de reserva
    
    // Agrega un evento de clic a cada botón
    boton.addEventListener('click', () => {
        // Si el botón ya está seleccionado, lo deseleccionamos
        if (boton.classList.contains('seleccionado')) {
            boton.classList.remove('seleccionado');
            boton.style.border = ''; // Elimina el borde especial

            // Ocultamos el campo fields[3] y reiniciamos los valores de los inputs dentro de él
            fields[3].classList.remove('visible');
            const inputsField3 = fields[3].querySelectorAll("input, textarea");
            inputsField3.forEach(input => input.value = '6'); // Reinicia los valores de los inputs dentro de fields[3]

            // Ocultamos el campo fields[4] y reiniciamos los valores de los inputs dentro de él
            fields[4].classList.remove('visible');
            const inputsField4 = fields[4].querySelectorAll("input, textarea");
            inputsField4.forEach(input => input.value = ''); // Reinicia los valores de los inputs dentro de fields[4]

            // Deshabilitar el botón de reservar y desactivar el hover
            botonReservar.disabled = true;
            botonReservar.style.opacity = '0.5'; // Transparente
            botonReservar.style.cursor = 'not-allowed'; // Cursor no permitido
        } else {
            // Si no está seleccionado, deseleccionamos todos los botones primero
            document.querySelectorAll('.consola-button').forEach(otroBoton => {
                otroBoton.classList.remove('seleccionado');
                otroBoton.style.border = ''; // Restablece todos los botones
            });
            
            // Luego, seleccionamos el botón que fue clickeado
            boton.classList.add('seleccionado');
            boton.style.border = '2px solid lime'; // Agrega el borde verde fosforescente

            // Mostramos el campo fields[3] y reiniciamos sus valores
            fields[3].classList.add('visible');
            const inputsField3 = fields[3].querySelectorAll("input, textarea");
            inputsField3.forEach(input => input.value = '6'); // Reinicia los valores de los inputs dentro de fields[3]
            
            // Mostramos el campo fields[4] y reiniciamos sus valores
            fields[4].classList.add('visible');
            const inputsField4 = fields[4].querySelectorAll("input, textarea");
            inputsField4.forEach(input => input.value = ''); // Reinicia los valores de los inputs dentro de fields[4]

            // Habilitar el botón de reservar y activar el hover
            botonReservar.disabled = false;
            botonReservar.style.opacity = '1'; // Restaurar visibilidad
            botonReservar.style.cursor = 'pointer'; // Cursor normal
        }
    });
});
