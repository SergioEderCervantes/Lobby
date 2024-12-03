document.addEventListener("DOMContentLoaded", () => {
    const accordionHeaders = document.querySelectorAll(".accordion_header");

    accordionHeaders.forEach(header => {
        header.addEventListener("click", () => {
            const content = header.nextElementSibling;
            // const item = header.parentElement;
            // Cerrar todos los contenidos excepto el actual
            document.querySelectorAll(".accordion_content").forEach(otherContent => {
                if (otherContent !== content) {
                    otherContent.classList.remove("open");
                    otherContent.previousElementSibling.classList.remove("active"); // Quitar clase activa de los headers
                }
            });

            // Alternar la visibilidad del contenido actual
            content.classList.toggle("open");
            header.classList.toggle("active"); // Cambiar el estado del ícono
        });
    });
});

console.log("HOLA")