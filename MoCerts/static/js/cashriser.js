let typeForm = document.querySelector('#id_type')
let emailForm = document.querySelector('#id_user')
let amountForm = document.querySelector('#id_amount')


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


function copyToClipboard(element) {
    id = '#' + element 
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(id).text()).select();
    document.execCommand("copy");
    $temp.remove();
}