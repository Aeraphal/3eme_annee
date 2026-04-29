

let img = new Image();   // Crée un nouvel élément Image
img.src = "../../Code/Images/Goblin_retouche.png";
var image2 =document.querySelector("#image2");
var canvas = document.querySelector("canvas");

var ctx =canvas.getContext("2d");

ctx.drawImage(
    image,0,0
)
ctx.drawImage(
    image2,0,75,100,100
)