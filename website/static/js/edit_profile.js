let input =  document.getElementById('last_name')
for (let i = 0; i < document.getElementsByClassName('choice').length; i++) {
    document.getElementsByClassName('choice')[i].style.width = (input.clientWidth - 24/2).toString() + "px"
}


function chooseRole(role) {
    var choice = "Student"
    var choice1 = "Teacher"
    if (choice !== role){
        choice1 = choice
    }
    if (document.getElementById(choice1.toLowerCase() + '_choice').classList.value.includes("chosen")){
        document.getElementById(choice1.toLowerCase() + '_choice').classList.remove("chosen")
    }
    document.getElementById('role').value = role;
    document.getElementById(role.toLowerCase() + '_choice').classList.add("chosen")
}


function changeUsername() {
    console.log("USERNAMEECHANGEEEEEEEEEEEE")
}


function changeEmail() {
    console.log("EMAILLLLCHANGEEEEEEEEEEEE")
}


function changePassword() {
    console.log("PASSWORDDDDCHANGEEEEEEEEEEEE")

}

