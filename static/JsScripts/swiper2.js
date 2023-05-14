const swiper2 = new Swiper('.swiper2', {

    loop: true,

    navigation: {
        nextEl: '.swiper-button-next2',
        prevEl: '.swiper-button-prev2',
    },

    slidesPerView: 1,
    spaceBetween: 10,

    breakpoints: {

        700: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        1000: {
            slidesPerView: 4,
            spaceBetween: 40
        },
    }

});