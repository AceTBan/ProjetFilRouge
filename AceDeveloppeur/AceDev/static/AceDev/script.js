
// ---------------------Swiper générale----------------------

const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    autoplay: true,
    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    
    // And if we need scrollbar
    scrollbar: {
    el: '.swiper-scrollbar',
    },

    speed: 2000,
    effect: 'fade',
    fadeEffect: {
    crossFade: true,
    },
});