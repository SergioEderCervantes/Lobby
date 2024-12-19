const termsButton = document.getElementById('termsButton');
const termsModal = document.getElementById('termsModal');
const closeModal = document.getElementById('closeModal');
const toggleInput = document.getElementById('toggle'); // El toggle
const inscribirseButton = document.getElementById('tournament_register_btn'); 

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
    inscribirseButton.classList.remove("disabled");
    inscribirseButton.disabled = false; // Activa el botón de reserva
    inscribirseButton.style.opacity = '1'; // Totalmente visible
    inscribirseButton.style.cursor = 'pointer'; // Cursor de puntero para indicar interactividad
    
  } else {
    inscribirseButton.classList.add("disabled");
    inscribirseButton.disabled = true; // Desactiva el botón de reserva
    inscribirseButton.style.opacity = '0.5'; // Transparente
    inscribirseButton.style.cursor = 'not-allowed'; // Cursor no permitido


  }
});

// Asegúrate de que el botón de reserva esté desactivado al principio si el toggle no está activado
if (!toggleInput.checked) {
  inscribirseButton.disabled = true;
}
