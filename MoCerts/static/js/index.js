const slides = document.querySelectorAll('.image-slider__image')
const videoPlayer = document.querySelector('.video-block video')
const playBtn = document.querySelector('.play-btn')
const houseIcon = document.querySelector('#home-icon');
// const sideBar = document.querySelector('.sidebar')
// const nav = document.querySelector('nav')
// console.log(nav)


const sideBarMini = sideBar.cloneNode(true)

playBtn.addEventListener('click', playVideo)
videoPlayer.addEventListener('ended', restartVideo)

 // show form filter user for generate sertificate

let i = 0
startSlider();
prepareSideBarMini()

const menuItems = sideBar.querySelectorAll('li')
const miniMenuItems = sideBarMini.querySelectorAll('li')
for (let i = 0; i < menuItems.length; i++) {
  menuItems[i].addEventListener('mouseover', () => i != 0 && mouseOver(i))
  menuItems[i].addEventListener('mouseout', () => i != 0 && mouseOut())
}
for (let i = 0; i < miniMenuItems.length; i++) {
  miniMenuItems[i].addEventListener('mouseover', () => i != 0 && mouseOver(i))
  miniMenuItems[i].addEventListener('mouseout', () => i != 0 && mouseOut())
}


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

function mouseOver(menuItem) {
  sideBarMini.querySelectorAll('.icon-back')[menuItem - 1].style.backgroundColor = '#5093d3';
  sideBarMini.querySelectorAll('.icon')[menuItem - 1].style.backgroundColor = '#5093d3';
  sideBar.querySelectorAll('li')[menuItem].style.backgroundColor = '#3F85CE';
  sideBar.querySelectorAll('a')[menuItem - 1].style.color = '#fff';
}
function mouseOut() {
  sideBarMini.querySelectorAll('.icon-back').forEach(menuItem => menuItem.style.backgroundColor = '#161717')
  sideBarMini.querySelectorAll('.icon').forEach(menuItem => menuItem.style.backgroundColor = '#2C2C2C')
  sideBar.querySelectorAll('li:not(.user)').forEach(menuItem => menuItem.style.backgroundColor = '#212121')
  sideBar.querySelectorAll('a').forEach(menuItem => menuItem.style.color = '#f3f0ea')
}

// function toggleSideBar() {
//   sideBar.classList.toggle('open')
//   nav.classList.toggle('navopen')
//   sideBarMini.classList.toggle('down')
// }

function playVideo() {
  playBtn.style.display = 'none'
  videoPlayer.play()
}
function restartVideo() {
  playBtn.style.display = 'inline'
}

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

function prepareSideBarMini() {
  sideBarMini.removeChild(sideBarMini.querySelector('.nav-controller'))
  sideBarMini.removeChild(sideBarMini.querySelector('.user'))
  sideBarMini.querySelectorAll('span').forEach(span => span.remove())
  sideBarMini.classList.add('sidebar-mini');

  const crown = document.createElement('li');
  crown.classList.add('crown');

  sideBarMini.insertBefore(crown, sideBarMini.firstChild)
  // sideBarMini.querySelector('.crown').appendChild(document.querySelector('.nav-controller').cloneNode(true))


  document.querySelector('nav').appendChild(sideBarMini);
}


// ScrollTop

let mybutton = document.getElementById("scrollBtn");
let mainSection = document.getElementById('first-section').scrollHeight;

window.onscroll = function() {scrollFunction()};

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




//const sideBarMini = sideBar.cloneNode(true)
//
//playBtn.addEventListener('click', playVideo)
//videoPlayer.addEventListener('ended', restartVideo)
//
//  show form filter user for generate sertificate


