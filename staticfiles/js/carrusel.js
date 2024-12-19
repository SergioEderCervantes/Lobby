var swiper = new Swiper(".swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true, // Centra la diapositiva activa
    spaceBetween: 20, // Espacio entre las diapositivas
    slidesPerView: 'auto', // Permite que la diapositiva activa sea visible completamente y la siguiente parcialmente
    initialSlide: 2, // Comienza desde la tercera diapositiva
    speed: 600, // Velocidad de la transición
    loop: true, // Activa el loop para que sea circular
    preventClicks: true, // Previene clics durante el movimiento
    coverflowEffect: {
        rotate: 0,
        stretch: 80, // Desplaza las diapositivas lateralmente
        depth: 350, // Profundidad de las diapositivas
        modifier: 1,
        slideShadows: true,
    },
    autoplay: {
        delay: 10000, // Tiempo entre transiciones automáticas (en milisegundos)
        disableOnInteraction: false, // El autoplay no se detiene al interactuar
    },
    pagination: {
        el: ".swiper-pagination", // Habilita la paginación
        clickable: true, // Permite clics en los puntos de paginación
    },
});