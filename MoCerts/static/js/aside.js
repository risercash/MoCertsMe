const aside__nav = document.querySelector('.aside__nav')
const asideController = document.querySelector('.aside__controller')
const crown = document.querySelector('.crown')
const icons = document.querySelector('.icons')
const iconSpans = document.querySelectorAll('.icons span')
const balanceBlock = document.querySelector('.balance-block')
console.log(balanceBlock)


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
        balanceBlock.classList.toggle('open')
        asideController.classList.toggle('open')
    }, 100)

}