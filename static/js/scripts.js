function menu() {
    var e1 = document.getElementById("menu");
    var e2 = document.getElementById("generic");
    if (e1.className === "navbar") {
        e1.className += " responsive";
    } else {
        e1.className = "navbar";
    }
}