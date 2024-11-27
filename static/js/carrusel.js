var swiper = new Swiper (".swiper" , {
    effect: "coverflow",
    grabCursor: true,
    centerSlides: true,
    spaceBetween: 20,
    initialSlide: 2,
    speed: 600,
    loop: true,
    preventClicks: true,
    slidespreview: 'auto',
    coverflowEffect: {
        rotate: 0,
        stretch: 80,
        depth: 350,
        modifier: 1,
        slideShadows: true,
    },
    on: {
        click(event){
            swiper.slideTo(this.clickedIndex)
        },
    },
    pagination: {
        el: ".swiper-pagination",
    },
    autoplay: {
        delay: 10000, // Tiempo entre transiciones (en milisegundos)
        disableOnInteraction: false, // El autoplay no se detiene si el usuario interactúa
    },
});

