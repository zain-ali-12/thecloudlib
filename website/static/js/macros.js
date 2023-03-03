var navbar_profile = document.getElementById("navbar_profile")
navbar_profile.addEventListener("mouseover", colorise)
function colorise() {
    navbar_profile.children[1].style.color = "#dc9860"
}
navbar_profile.addEventListener("mouseout", decolorise)
function decolorise() {
    navbar_profile.children[1].style.color = "#e0e0e0"
}

var profile_image = document.getElementById("navbar_profile");
profile_image.addEventListener("click", display_profile);
document.getElementById('profile-popup-container').addEventListener("click", close_profile);

function display_profile() {
    var user_profile = document.getElementById('profile-popup-container');
    user_profile.style.display = "block";
}
function close_profile(e) {
    if (e.target.id == "profile-popup-container") {
        document.getElementById("profile-popup-container").style.display = 'none';
    }
}
