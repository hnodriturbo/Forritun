// Variables

// Canvas and Context
const canvas = document.getElementById("myPacManGame");
const ctx = canvas.getContext("2d");

// Pac-Man Colors
const pacManColor = "yellow";
const pacManEyeColor = "black";

// Pac-Man Parameters
const pacManX = 12;
const pacManY = 12;
const pacManRadius = 150;
const pacManMouthStartAngle = Math.PI / 7;
const pacManMouthEndAngle = -Math.PI / 7;

function drawPacMan() {
    ctx.beginPath();
    ctx.arc(37, 37, 13, Math.PI / 7, -Math.PI / 7, false);
    ctx.lineTo(31, 37);
    ctx.fill();
}

// Ghost Colors
const ghostBodyColor = "blue";
const ghostEyeColor = "white";

// Ghost Parameters
const ghostX = [53, 135];
const ghostY = [53, 119];
const ghostWidth = [49, 25];
const ghostHeight = [33, 49];
const ghostEyeRadius = 4;

// Maze Wall Color
const mazeWallColor = "blue";

// Maze Wall Parameters
const wallX = [12, 19, 53, 135];
const wallY = [12, 19, 53, 119];
const wallWidth = [150, 150, 49, 49];
const wallHeight = [150, 150, 33, 49];
const wallRadius = [15, 9, 10, 10];

// Maze Dots Color
const dotColor = "white";
const dotSize = 4;


function drawWalls() {
    /* First roundedRect that is the outer wall */
    roundedRect(ctx, 5, 5, 740, 540, 15);
    /* Second roundedRect that is the inner wall */
    roundedRect(ctx, 10, 10, 730, 530, 9);

    /* ----- Walls in column 1 ----- */
    roundedRect(ctx, 53, 53, 49, 33, 10);
    roundedRect(ctx, 53, 119, 49, 16, 6);
    roundedRect(ctx, 53, 162, 49, 120, 6);


    /* ----- Walls in column 2 ----- */     
    roundedRect(ctx, 135, 53, 49, 33, 10);
    roundedRect(ctx, 135, 119, 25, 49, 10);

    /* Big wall on right side */
    roundedRect(ctx, 400, 50, 100, 150, 15);
    roundedRect(ctx, 400, 300, 100, 150, 15);


            
}



function drawGhosts() {
    /* The ghost */
    ctx.beginPath();
    ctx.moveTo(83, 116);
    ctx.lineTo(83, 102);
    ctx.bezierCurveTo(83, 94, 89, 88, 97, 88);
    ctx.bezierCurveTo(105, 88, 111, 94, 111, 102);
    ctx.lineTo(111, 116);
    ctx.lineTo(106.333, 111.333);
    ctx.lineTo(101.666, 116);
    ctx.lineTo(97, 111.333);
    ctx.lineTo(92.333, 116);
    ctx.lineTo(87.666, 111.333);
    ctx.lineTo(83, 116);
    ctx.fill();

    /* The eyes of the ghos */
    ctx.fillStyle = "white";
    ctx.beginPath();
    ctx.moveTo(91, 96);
    ctx.bezierCurveTo(88, 96, 87, 99, 87, 101);
    ctx.bezierCurveTo(87, 103, 88, 106, 91, 106);
    ctx.bezierCurveTo(94, 106, 95, 103, 95, 101);
    ctx.bezierCurveTo(95, 99, 94, 96, 91, 96);
    ctx.moveTo(103, 96);
    ctx.bezierCurveTo(100, 96, 99, 99, 99, 101);
    ctx.bezierCurveTo(99, 103, 100, 106, 103, 106);
    ctx.bezierCurveTo(106, 106, 107, 103, 107, 101);
    ctx.bezierCurveTo(107, 99, 106, 96, 103, 96);
    ctx.fill();
    

    /* The eyes stones of the ghost */
    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.arc(101, 102, 2, 0, Math.PI * 2, true);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(89, 102, 2, 0, Math.PI * 2, true);
    ctx.fill();
}

function draw() {
    const canvas = document.getElementById("myPacManGame");
    if (canvas.getContext) {
        const ctx = canvas.getContext("2d");
    
        drawWalls();
        drawPacMan();
        drawGhosts();


    
        for (let i = 0; i < 8; i++) {
            ctx.fillRect(51 + i * 16, 35, 4, 4);
        }
    
        for (let i = 0; i < 6; i++) {
            ctx.fillRect(115, 51 + i * 16, 4, 4);
        }
    
        for (let i = 0; i < 8; i++) {
            ctx.fillRect(51 + i * 16, 99, 4, 4);
        }
    


    }
  }
  
  // A utility function to draw a rectangle with rounded corners.
  
  function roundedRect(ctx, x, y, width, height, radius) {
    ctx.beginPath();
    ctx.moveTo(x, y + radius);
    ctx.arcTo(x, y + height, x + radius, y + height, radius);
    ctx.arcTo(x + width, y + height, x + width, y + height - radius, radius);
    ctx.arcTo(x + width, y, x + width - radius, y, radius);
    ctx.arcTo(x, y, x, y + radius, radius);
    ctx.stroke();
  }
  

draw();

roundedRect();

ctx.beginPath();
ctx.rect(10, 10, 700, 600);
ctx.stroke();


/* The function and the loop to play the game */
function updateGame() {
    clearCanvas();
    drawBoard();
    drawPacMan();
    drawGhosts();
    updatePositions();
    checkCollisions();
    requestAnimationFrame(updateGame);
}

requestAnimationFrame(updateGame);