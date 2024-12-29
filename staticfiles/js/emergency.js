document.addEventListener("DOMContentLoaded", () => {
    // Selecciona el elemento
    const bodySection = document.querySelector('.body');

    // Obtén la URL de la imagen
    const imageUrl = bodySection.dataset.bg;

    // Asigna la URL como fondo del elemento
    bodySection.style.backgroundImage = `url('${imageUrl}')`;
    bodySection.classList.add("emergency")
})