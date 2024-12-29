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

// Temita de los corazones

if (num_torneos != 0){

    const heart_disp = document.getElementById("heart-display");
    const red_hearts = heart_disp.querySelectorAll(".heart-red");
    const grey_hearts = heart_disp.querySelectorAll(".heart-gray");
    for (let i = 0; i < num_torneos; i++) {
        console.log("hola");
        const red_heart = red_hearts[i];
        const gray_heart = grey_hearts[i];
        red_heart.classList.remove("hidden");
        gray_heart.classList.add("hidden");
    }

}