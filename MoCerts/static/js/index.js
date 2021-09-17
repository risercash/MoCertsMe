const slides = document.querySelectorAll('.image-slider__image')
// const houseIcon = document.querySelector('#home-icon');

let i = 0
startSlider();

let swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    1601: {
      slidesPerView: 2,
      spaceBetween: 20
    },
  },
  loop: true,
  speed: 1000,
  autoplay: true
});

async function startSlider() {
  if (!slides[i]) {
    i = 0;
  }
  document.querySelector('.intro').classList.add('go')
  slides.forEach(slide => {
    slide.style.visibility = "hidden"
    slide.style.transform = "scale(1.2)"
  })
  slides[i].style.visibility = 'visible'
  slides[i].style.transform = "scale(1)"
  let promise = new Promise((resolve, reject) => {

    setTimeout(() => resolve(slides[i]), 30000)
  });

  setTimeout(() => document.querySelector('.intro').classList.remove('go'), 28000)
  await promise
  i++
  startSlider()
}

// ScrollTop

let mybutton = document.getElementById("scrollBtn");
let mainSection = document.getElementById('first-section').scrollHeight;

window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > mainSection || document.documentElement.scrollTop > mainSection) {
    mybutton.classList.add('add-effect');
  } else {
    mybutton.classList.add('none-effect');
    mybutton.classList.remove('add-effect');
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


// Позже удалю
// const videoPlayer = document.querySelector('.video-block video')
// const playBtn = document.querySelector('.play-btn')
// playBtn.addEventListener('click', playVideo)
// videoPlayer.addEventListener('ended', restartVideo)

// function playVideo() {
//   playBtn.style.display = 'none'
//   videoPlayer.play()
// }
// function restartVideo() {
//   playBtn.style.display = 'inline'
// }