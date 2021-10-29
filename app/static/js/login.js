window.addEventListener('DOMContentLoaded', event => {

    const btn_register = document.body.querySelector('#registerForm');
    const btn_login = document.body.querySelector('#login');

    const form_login = document.body.querySelector('#sign-in');
    const form_register = document.body.querySelector('#sign-up');
    if (btn_register)
    {
        btn_register.addEventListener('click', e => {
            if (form_login) form_login.style.display = "none";
            form_register.style.display = "block";
        });
    }

    if (btn_login)
    {
        btn_login.addEventListener('click', e =>{
            if (form_register) form_register.style.display = "none";
            form_login.style.display = "block";
        });
    }

});