const ubicacionContenedor = document.querySelector('.ubicacion');
let Animated = false; // Variable para asegurar que la animación solo se ejecute una vez

// Función para verificar si el contenedor está en la vista
function check() {
  const rect = ubicacionContenedor.getBoundingClientRect();
  const windowHeight = window.innerHeight;

  // Si el contenedor está en la vista y no ha sido animado previamente
  if (rect.top < windowHeight - rect.height / 2 && !Animated) {
    ubicacionContenedor.classList.add('show'); // Agregar la clase para activar la animación
   
    Animated = true; // Marcar que ya se ha animado
  }
}

// Ejecutar la función al hacer scroll
window.addEventListener('scroll', check);

// Llamar a la función al cargar la página para verificar si ya está visible
check();
