var i = 0;
var title = "Articulate.";
var speed = 70;

function typeWriter() {
    if(i < title.length) {
        document.getElementById('title').innerHTML += title.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

