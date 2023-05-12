const swiper = new Swiper('.swiper', {

    loop: true,

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    slidesPerView: 4,
    spaceBetween: 10,
    // Responsive breakpoints
    // breakpoints: {
    //     700: {
    //         slidesPerView: 3,
    //         spaceBetween: 30
    //     },
    //     1000: {
    //         slidesPerView: 4,
    //         spaceBetween: 40
    //     },
    //     1300: {
    //         slidesPerView: 5,
    //         spaceBetween: 50
    //     },
    //     1400:{
    //         slidesPerView: 6,
    //         spaceBetween: 60
    //     },
    //     1600: {
    //         slidesPerView: 7,
    //         spaceBetween: 70
    //     }
    // }

});