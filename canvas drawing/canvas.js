/* Hreiðar Pétursson 23 janúar 2024 */

var canvas = document.querySelector('canvas');  

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext("2d");


// Breyta litnum
c.fillStyle = 'rgba(255, 0, 0, 0.2)'; // Rauður
// Bý til ferhyrninginn 
// Values = 1&2=Location - 3&4=Size
c.fillRect(100, 100, 100, 100);


// Ferningur 2
c.fillStyle = 'rgba(0, 255, 0, 0.6)'; // Grænn
c.fillRect(400, 100, 100, 100);


// Ferningur 3
c.fillStyle = 'rgba(0, 0, 255, 0.8)'; // Blár
c.fillRect(300, 300, 100, 100);

console.log(canvas)

// Line
c.beginPath();
c.moveTo(50, 300);

// Need to use stroke method to see
c.lineTo(300, 100);
c.lineTo(400, 300);

// Change the color of the line
c.strokeStyle = "#fa34a3";

c.stroke();

/* 
// Arc / Circle
c.beginPath();

c.arc(200, 300, 30, 
    0, Math.PI * 2, 
    false);

c.strokeStyle = 'blue';
// Must use stroke to draw
c.stroke();

 */

/* - This are the value of a arc
c.arc(x: number, y: number, radius: number, startAngle: number, 
    endAngle: number, counterclockwise?: boolean | undefined)
*/

colors = ['red', 'green', 'blue']

for (var i = 0; i < 100; i++) {

    var x = Math.random() * window.innerWidth;
    var y = Math.random() * window.innerHeight;

    // Arc / Circle
    c.beginPath();

    c.arc(x, y, 30, 
        0, Math.PI * 2, 
        false);

    c.strokeStyle = 'blue';
    // Must use stroke to draw
    c.stroke();
}


