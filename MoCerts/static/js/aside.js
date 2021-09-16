const aside__nav = document.querySelector('.aside__nav')
const aside__controller = document.querySelector('.aside__controller')
const crown = document.querySelector('.crown')
const icons = document.querySelector('.icons')
const iconSpans = document.querySelectorAll('.icons span')
console.log(iconSpans)


function toggleSideBar() {
    iconSpans.forEach(iconSpan => {
        if (iconSpan.classList.contains('icon_zIndex')) {
            iconSpan.classList.remove('icon_zIndex')
        } else {
            setTimeout(() => {
                iconSpan.classList.add('icon_zIndex')
            }, 600)
        }
    })
    setTimeout(() => {
        aside__nav.classList.toggle('open')
        icons.classList.toggle('open')
        crown.classList.toggle('open')
        aside__controller.classList.toggle('open')
    }, 100)

}