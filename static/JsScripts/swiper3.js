const swiper3 = new Swiper('.swiper3', {

    loop: true,

    navigation: {
        nextEl: '.swiper-button-next3',
        prevEl: '.swiper-button-prev3',
    },

    slidesPerView: 1,
    spaceBetween: 10,
    // Responsive breakpoints
    breakpoints: {
        // when window width is >= 320px
        500: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        // when window width is >= 480px
        700: {
            slidesPerView: 3,
            spaceBetween: 30
        },
    }

});