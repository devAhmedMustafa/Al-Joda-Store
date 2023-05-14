const swiper1 = new Swiper('.swiper1', {

    loop: true,

    navigation: {
        nextEl: '.swiper-button-next1',
        prevEl: '.swiper-button-prev1',
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
        // when window width is >= 640px
        1000: {
            slidesPerView: 4,
            spaceBetween: 40
        },
        1300: {
            slidesPerView: 5,
            spaceBetween: 50
        },
        1400:{
            slidesPerView: 6,
            spaceBetween: 60
        },
        1600: {
            slidesPerView: 7,
            spaceBetween: 70
        }
    }

});