
// Función para verificar si el elemento está en la vista
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return rect.top >= 0 && rect.bottom <= window.innerHeight;
  }
  
  // Aplicar clase 'visible' cuando el elemento esté en la vista
  const elements = document.querySelectorAll('.torneo_home');
  
  window.addEventListener('scroll', () => {
    elements.forEach(element => {
      if (isInViewport(element)) {
        element.classList.add('visible');
      }
    });
  });
  