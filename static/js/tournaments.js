document.addEventListener("DOMContentLoaded", function () {
    const imageContainers = document.querySelectorAll(".container");
    if (imageContainers){
        imageContainers.forEach(container => {
            const img = container.querySelector("img");
            const loader = container.querySelector(".wrapper");
    
            img.onload = () => {
                loader.style.display = "none"; // Oculta el loader
                img.classList.remove("hidden"); // Muestra la imagen
                img.classList.add("loaded"); // Añade la clase para el estilo final
            };
    
            // Por si la imagen ya está en caché
            if (img.complete) {
                img.onload();
            }
        });

    }

    const backgroundImages = document.querySelectorAll(".background_image, .banner_image");

    if (backgroundImages){
        backgroundImages.forEach(container => {
            const img = container.querySelector("img");
            const loader = container.querySelector(".wrapper");
    
            img.onload = () => {
                loader.style.display = "none"; // Oculta el loader
                img.classList.remove("hidden"); // Muestra la imagen
                img.classList.add("loaded"); // Añade la clase para el estilo final
            };
    
            // Por si la imagen ya está en caché
            if (img.complete) {
                img.onload();
            }
        });
    }
});