let buttons = document.querySelectorAll("[id^='b']");

buttons.forEach(button => {
    button.addEventListener("click", function() {
        let id = this.id.replace('b', '');
        document.querySelectorAll(".hide").forEach(hide => {hide.style.display = "none"});
        document.getElementById(id).style.display = "block";
    });
});


document.querySelectorAll(".hide").forEach(hide => {hide.style.display = "none"});
document.getElementById("1").style.display = "block";





