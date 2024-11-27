document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.querySelector(".navbar");
    const landpage = document.querySelector(".landpage");

    // Si la landing page no existe (páginas como Restaurante, etc.)
    if (!landpage) {
        navbar.classList.add("sticky"); // Fija la navbar automáticamente
        return;
    }

    // Si hay una landing page, manejar la transición entre estados
    document.addEventListener("scroll", () => {
        const landBottom = landpage.getBoundingClientRect().bottom;

        if (landBottom <= 125 ) {
            // Cambia el estilo de la navbar cuando la landing page desaparezca
            navbar.classList.add("sticky");
        } 
        else {
            // Restaura el estilo de la navbar mientras la landing page esté visible
            navbar.classList.remove("sticky");
        }
    });
});
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
