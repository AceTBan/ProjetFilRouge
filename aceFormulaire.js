let area = document.querySelector("textarea");
let button = document.querySelector("button");
area.addEventListener("keyup",function () {
if (area.value.length >= 5) {
    button.disabled = true; 
} else {
    button.disabled = false;
}
})