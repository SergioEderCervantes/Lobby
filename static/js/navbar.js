
 const icons = document.querySelectorAll('.icon');

 icons.forEach(icon => {
     const image = icon.querySelector('img');
     const hoverSrc = image.getAttribute('data-hover');
     const defaultSrc = image.getAttribute('data-default');

     icon.addEventListener('mouseenter', () => {
         image.src = hoverSrc; // Cambia al ícono a color
        
     });

     icon.addEventListener('mouseleave', () => {
         image.src = defaultSrc; // Cambia de regreso al ícono en blanco y negro
     });
 });

 const menu = document.querySelector('.menu');
const section = document.querySelector('.navbar .section');
 menu.addEventListener("click", function() {
    
        menu.classList.toggle('active');
        section.classList.toggle('active');
  });