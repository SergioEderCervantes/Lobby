// Obtener los elementos
const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");
const body = document.body;


// Función para abrir y cerrar la barra lateral
menuToggle.addEventListener("click", function() {
    // Alternar la clase "open" en el sidebar
    sidebar.classList.toggle("open");
    
   
   
});

