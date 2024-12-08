// Obtener el contenedor y el texto
const contenedor = document.querySelector('.contenedor_h');
const contenedor2 = document.querySelector('.contenedor_h2');
const texto = document.getElementById('texto');
const texto2 = document.getElementById('texto2');

// Agregar el evento hover (mouseenter y mouseleave)
contenedor.addEventListener('mouseenter', () => {
    // Mover el texto a una nueva posición
    texto.style.top = '65%'; // Cambiar la posición vertical
    texto.style.transition = 'all 0.5s';
});

contenedor.addEventListener('mouseleave', () => {
    // Regresar el texto a su posición original
    texto.style.top = '80%'; 
    texto.style.transition = 'all 0.5s';
   
});
contenedor2.addEventListener('mouseenter', () => {
    // Mover el texto a una nueva posición
    texto2.style.top = '65%'; // Cambiar la posición vertical
    texto2.style.transition = 'all 0.5s';
});

contenedor2.addEventListener('mouseleave', () => {
    // Regresar el texto2 a su posición original
    texto2.style.top = '80%'; 
    texto2.style.transition = 'all 0.5s';
   
});

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
  