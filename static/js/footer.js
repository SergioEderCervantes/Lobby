
const pacman = document.getElementById('pacman');
const sections = document.querySelectorAll('.content-icon');
let moved = false; // Variable para alternar estado
let isMobile = window.matchMedia('(max-width: 767px)').matches; // Detectar si es móvil al cargar

// Función para manejar el clic en pacman
function handlePacmanClick() {
  
  if (!isMobile) return; // Si no es móvil, no hacer nada

  if (!moved) {
    pacman.style.transform = 'translateY(-10%)';
  } else {
    pacman.style.transform = 'translateY(120px)';
  }

  sections.forEach((section) => {
    section.classList.toggle('active');
  });

  moved = !moved; // Cambiar el estado
}

// Escuchar el clic en pacman solo si es móvil
pacman.addEventListener('click', handlePacmanClick);

// Detectar cambios en el tamaño de la pantalla
window.addEventListener('resize', () => {
  isMobile = window.matchMedia('(max-width: 767px)').matches; // Actualizar si es móvil
});

// Función para activar la vibración
function startVibration() {
  pacman.classList.add('vibrate'); // Agrega la clase que activa la animación

  setTimeout(() => {
    pacman.classList.remove('vibrate'); 
  }, 500); 
}

  setInterval(() => {
    if(!moved){
      if (Math.random() > 0.3) { // Probabilidad del 30% de vibrar cada 5 segundos
        startVibration();
      }
    }
  }, 2000);


