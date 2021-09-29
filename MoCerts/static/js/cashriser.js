let typeForm = document.querySelector('#id_type')
let emailForm = document.querySelector('#id_user')


function readonlyForm () {
    if (typeForm.value == 'regular') {
        emailForm.readOnly = true;
        emailForm.style.backgroundColor = 'rgb(177 177 177)';
    } else {
        emailForm.readOnly = false;
        emailForm.style.backgroundColor = 'rgb(255, 255, 255)';
    }
}


typeForm.addEventListener('change', function (e) {
    readonlyForm ()
})

readonlyForm ()


