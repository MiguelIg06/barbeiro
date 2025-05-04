// Aplicar a animção nos campos de entrada
function toggleAnimation(){
    const userName = document.getElementById('email');
    const password = document.getElementById('password');
    const userNameLabel = document.getElementById('email-label');
    const passwordLabel = document.getElementById('password-label');

    userName.addEventListener("focus", () =>{
        userNameLabel.classList.remove('login-label-empty');
        userNameLabel.classList.add('login-label');
    })

    userName.addEventListener("blur", () =>{
        if(userName.value === ""){
            userNameLabel.classList.remove('login-label');
            userNameLabel.classList.add('login-label-empty');
        }
    })

    password.addEventListener("focus", () =>{
        passwordLabel.classList.remove('login-label-empty');
        passwordLabel.classList.add('login-label');
    })

    password.addEventListener("blur", () =>{
        if(password.value === ""){
            passwordLabel.classList.remove('login-label');
            passwordLabel.classList.add('login-label-empty');
        }
    })
}

toggleAnimation();


// Mostra a senha ao clicar no botão
function showPassword(){
    const showPasswordButton = document.querySelector("#eye-icon");
    const password = document.getElementById('password');

    showPasswordButton.addEventListener("click", () =>{
        if(password.type === "password"){
            password.type = "text";
            showPasswordButton.classList.remove("fa-eye-slash");
            showPasswordButton.classList.add("fa-eye");
        } else{
            password.type = "password";
            showPasswordButton.classList.remove("fa-eye");
            showPasswordButton.classList.add("fa-eye-slash");
        }
    })
}

showPassword();