const userFilter = document.querySelectorAll('.show_form_filter_user');
const is_namingCertificate = document.getElementById('horns');
const search_user = document.getElementById('search_user');

is_namingCertificate.addEventListener('change', function () {
    let chk = event.target
    if (chk.checked == true) {
        userFilter.forEach(item => {
            item.disabled = true;
        })
    } else {
        userFilter.forEach(item => {
            item.disabled = false;
        })
    }
})