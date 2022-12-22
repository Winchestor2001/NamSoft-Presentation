let leftBtn = document.querySelector(".left_btn")
let links = document.querySelector('.left_content')
let right_content = document.querySelector('.right_content')
let basic_li = document.querySelectorAll('.basic_li')
let drop_ul_li = document.querySelectorAll('.drop_ul_li')

drop_ul_li.forEach(elem =>{
    elem.addEventListener('click',()=>{
        ajaxGetter(elem.getAttribute('data-pk'));
        links.classList.toggle("left_active")
        right_content.classList.toggle('right_active')
    })
})

basic_li.forEach(elem =>{
    elem.addEventListener('click', ()=>{
        if (elem.nextElementSibling!=null) {
            elem.nextElementSibling.classList.toggle('drop_ul_active')
        }
    })
})
leftBtn.addEventListener('click', (e) => {
    links.classList.toggle("left_active")
    right_content.classList.toggle('right_active')
})


// window.onload = () => {
//     copyBtnFunc();
// }