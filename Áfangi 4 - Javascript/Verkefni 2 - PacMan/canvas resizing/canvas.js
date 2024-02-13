/* Hreiðar Pétursson 23 janúar 2024 */

var canvas = document.querySelector('canvas');  

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext("2d");

c.fillRect(100, 100, 100, 100);
c.fillRect(400, 100, 100, 100);
c.fillRect(300, 300, 100, 100);

console.log(canvas)