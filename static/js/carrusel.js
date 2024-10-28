let currentIndex = 0;
const images = document.querySelectorAll('.carousel-images img');
const totalImages = images.length;

function showSlide(index) {
    currentIndex = (index + totalImages) % totalImages; // Asegura que el índice sea válido
    const offset = -currentIndex * 100; // Mueve el carrusel
    document.querySelector('.carousel-images').style.transform = `translateX(${offset}%)`;
}

// Cambia la imagen automáticamente cada 3 segundos
setInterval(() => {
    showSlide(currentIndex + 1);
}, 3000);

function changeSlide(direction) {
    showSlide(currentIndex + direction);
}

// Muestra la primera imagen al cargar
showSlide(currentIndex);
