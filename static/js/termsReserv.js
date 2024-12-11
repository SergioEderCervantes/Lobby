const termsButton = document.getElementById('termsButton');
const termsModal = document.getElementById('termsModal');
const closeModal = document.getElementById('closeModal');
const toggleInput = document.getElementById('toggle'); // El toggle
const reserveButton = document.getElementById('register_reservation'); // El botón de reserva

// Función para abrir el modal
termsButton.addEventListener('click', () => {
  termsModal.style.display = 'block';
});

// Función para cerrar el modal
closeModal.addEventListener('click', () => {
  termsModal.style.display = 'none';
});

// Función para habilitar o deshabilitar el botón de reserva según el estado del toggle
toggleInput.addEventListener('change', () => {
  if (toggleInput.checked) {
    reserveButton.disabled = false; // Activa el botón de reserva
  } else {
    reserveButton.disabled = true; // Desactiva el botón de reserva
  }
});

// Asegúrate de que el botón de reserva esté desactivado al principio si el toggle no está activado
if (!toggleInput.checked) {
  reserveButton.disabled = true;
}
