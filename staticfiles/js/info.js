const infoSection = document.querySelector('.informacion_general');
let hasAnimated = false; // Variable para asegurar que la animación solo se ejecute una vez

// Función que detecta si el elemento está en la vista
function checkScroll() {
  const rect = infoSection.getBoundingClientRect();
  const windowHeight = window.innerHeight;

  // Si el elemento está al menos a la mitad de la ventana y no ha sido animado previamente
  if (rect.top < windowHeight - rect.height / 2 && !hasAnimated) {
    setTimeout(() => { // Agregar un retraso antes de activar la animación
      infoSection.classList.add('show'); // Agregar la clase para animar
      hasAnimated = true; // Marcar que ya se ha animado
    }, 200); // Retraso de 200ms antes de que comience la animación
  }
}

// Ejecutar la función al hacer scroll
window.addEventListener('scroll', checkScroll);

// Llamar a la función al cargar la página para verificar si ya está visible
checkScroll();
