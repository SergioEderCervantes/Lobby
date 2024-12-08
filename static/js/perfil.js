// Obtener los elementos
const menuToggle = document.getElementById("menu-toggle");

const sidebar = document.getElementById("sidebar");
const body = document.body;


// Función para abrir y cerrar la barra lateral
menuToggle.addEventListener("click", function() {
    // Alternar la clase "open" en el sidebar
    menuToggle.classList.toggle("active");
    sidebar.classList.toggle("open");
    
   
   
});

window.addEventListener('load', () => {
    const logo = document.querySelector('.imag');
     const landpage = document.querySelector(".landpage");

     if (landpage) {
          logo.classList.add('active');
         return;
     }

  });