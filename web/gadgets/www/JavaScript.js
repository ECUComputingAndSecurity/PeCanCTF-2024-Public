//Global variable declaration
var gadget_text = document.getElementById("gadget_text");
var text_size = 20

//Function that produces a random number
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

//Increases the size of the text by 4 pixels
document.getElementById("sizeUp").onclick = function() {
    text_size += 4;
    gadget_text.style.fontSize = text_size.toString() + 'px';
}

//Decreases the size of the text by 4 pixels
//Flag 3/3 '_w3b_d3v}'
document.getElementById("sizeDown").onclick = function() {
    text_size -= 4;
    gadget_text.style.fontSize = text_size.toString() + 'px';
}

//Makes the colour of the text change to a random colour
document.getElementById("colour").onclick = function() {
    var r = getRandomInt(220)
    var g = getRandomInt(220)
    var b = getRandomInt(220)
    gadget_text.style.color = 'rgb(' + r + ', ' + g + ', ' + b +')';
}

//Resets all changes made by the other functions
document.getElementById("reset").onclick = function() {
    gadget_text.style.color = '#222';
    gadget_text.style.fontSize = '20px';
    text_size = 20;
}