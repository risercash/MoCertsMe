const aside__nav = document.querySelector('.aside__nav')
const asideController = document.querySelector('.aside__controller')
const crown = document.querySelector('.crown')
const icons = document.querySelector('.icons')
const iconSpans = document.querySelectorAll('.icons span')
const balanceBlock = document.querySelector('.balance-block')

//раскрытие сайдбара
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
        asideController.classList.toggle('open')
        icons.classList.toggle('open')
        crown.classList.toggle('open')
        balanceBlock.classList.toggle('open')
    }, 100)

}

// изменение цвета надписей сайдбара при наведении
const menuItemsLi = icons.querySelectorAll('li')
const iconsItem = icons.querySelectorAll('.icons__item')

for (let i = 0; i < menuItemsLi.length; i++) {
    menuItemsLi[i].addEventListener('mouseover', () => {
        iconsItem[i].classList.add('hover')
        const icon__span = menuItemsLi[i].querySelector('.icon__span')
        icon__span.style.zIndex = 1
    })
    menuItemsLi[i].addEventListener('mouseout', () => {
        iconsItem[i].classList.remove('hover')
        const icon__span = menuItemsLi[i].querySelector('.icon__span')
        icon__span.style.zIndex = -1
    })
}


const dropdown_mobile = document.querySelectorAll('.dropdown_mobile')
dropdown_mobile.forEach(elem => elem.addEventListener("click", function(){ elem.style.zIndex = 99}))