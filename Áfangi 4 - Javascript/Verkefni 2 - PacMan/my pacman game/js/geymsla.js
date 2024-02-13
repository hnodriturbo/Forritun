

document.getElementById('playAgainButton').addEventListener('click', (event) => {restartGame();});


document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'ArrowLeft':
            pacMan.direction = 'left';
            break;
        case 'ArrowRight':
            pacMan.direction = 'right';
            break;
        case 'ArrowUp':
            pacMan.direction = 'up';
            break;
        case 'ArrowDown':
            pacMan.direction = 'down';
            break;
    }
});


function gameLoop() {
    // Start by clearing the canvas
    clearCanvas();
    console.log('cleared the canvas function called inside the gameLoop function')
    // Update game state
    updateGame();
    console.log('updateGame function being called')
    // Request Animation Framr for smoother animation
    requestId = requestAnimationFrame(gameLoop);
}

function initializeGame() {

    // Initialize game elements (ghosts, dots, etc.)
    initializeGhosts();
    console.log('Created the ghosts instances')

    // Create the dots instances and store in array
    prepareDots(); // Assuming this function is defined elsewhere to prepare dots
    console.log('prepared the dots to the array')

    // Start the game loop
    gameLoop();
    console.log('started the game loop function')
}



// This function draws constantly pacman, dots and ghosts.
function updateGame() {

    // Draw Pac-Man
    updatePacMan();
    // Draw dots
    updateDots();
    // Draw ghosts
    updateGhosts(ctx);

    

}


updatePacMan() {
    // Update Pac-Man's position based on current direction
    /* pacMan.move(); */

    if (!gamePaused || this.invulnerable) {
        pacMan.move();
    }
    // Check for collisions with the canvas boundaries and adjust Pac-Man's direction if necessary
    pacMan.canvasCollision();

    // Check for dot collision
    pacMan.checkDotCollisions();

    pacMan.checkGhostCollisions();

    // After updating position and handling collisions, draw Pac-Man on the canvas
    pacMan.draw(ctx);
}


            /* ----------------------------------------- */
            /* ---- Collision part of Pac-Man class ---- */
            /* ----------------------------------------- */
/* 
    // Method for collision of Pac-Man and the canvas walls
    canvasCollision() {
        // When pacman x (his center) reaches the 25px then put x position of pacman there
        if (this.x - this.radius <= 0) {
            this.x = this.radius; 
        } 
        if (this.x + this.radius >= canvasWidth) { 
            this.x = canvasWidth - this.radius; 
        }
        if (this.y - this.radius <= 0) { 
            this.y = this.radius; 
        }
        if (this.y + this.radius >= canvasHeight) { 
            this.y = canvasHeight - this.radius; 
        }
    },
    
 */




canvasCollisionDetection() {
    // Bounce off walls by reversing velocity
    if (this.x <= 0 || this.x + this.width >= canvasWidth) {
        /* this.x = this.x */
        this.vx = this.setRandomDirection();
    }

    if (this.y <= 0 || this.y + this.height >= canvasHeight) {
        this.vy = this.setRandomDirection();
    }
}







// Function for drawing the ghosts and update their position
function updateGhosts(ctx) {
    Object.values(ghosts).forEach(ghost =>  {
        ghost.canvasCollisionDetection();

        if (!gamePaused) {
            ghost.move(); // Move ghost only if game is not paused when pac-man dies
        }

        /* ghost.move(); */ // Update ghost's position
        ghost.draw(ctx) // Draw the ghost
    });
}



// Update Pac-Man's position and check for collisions
function updatePacMan() {
    // Update Pac-Man's position based on current direction
    /* pacMan.move(); */

    if (!gamePaused || this.invulnerable) {
        pacMan.move();
    }
    // Check for collisions with the canvas boundaries and adjust Pac-Man's direction if necessary
    pacMan.canvasCollision();

    // Check for dot collision
    pacMan.checkDotCollisions();

    pacMan.checkGhostCollisions();

    // After updating position and handling collisions, draw Pac-Man on the canvas
    pacMan.draw(ctx);
}

// Function to update the dots
function updateDots() {
    dots.forEach(dot => dot.draw(ctx));
}






checkGhostCollisions() {
    // Start to check if he is invulnerable and the ghost's can't hurt him.. only for respawning
    // and in case there is a ghost there
    if (this.invulnerable) {
        return;
    }

    //Extra threshold for Pac-Man's mouth 
    const mouthAdjustment = -5; 
    
    Object.values(ghosts).forEach(ghost => {
        // Calculate center of ghost (not the x corner of it)
        let ghostCenterX = ghost.x + ghost.width / 2;
        let ghostcenterY = ghost.y + ghost.height / 2;

        // Use the pythagoras to calculate distance between two objects
        let dx = this.x - ghostCenterX;
        let dy = this.y - ghostcenterY;
        let distance = Math.sqrt(dx * dx + dy * dy);


        // Adjustment variable thresholt
        let adjustment = 0;

        if ((this.direction === 'left' && dx > 0) ||
            (this.direction === 'right' && dx < 0) ||
            (this.direction === 'up' && dy > 0) ||
            (this.direction === 'down' && dy < 0)) {
            adjustment = mouthAdjustment;
        }
        
        if (distance < this.radius + ghost.radius + adjustment) {
            this.pacManDies();
        }

    });
},





/* 
    changeDirectionAvoidingWall(wallHit) {
        // Find current direction object
        const currentDir = this.directions.find(dir => dir.id === this.currentDirection.id);
        
        // Filter out directions leading back to the wall
        const validAlternatives = currentDir.alternatives.filter(alt => alt.indexOf(wallHit) === -1);
        
        // Randomly select a new direction from valid alternatives
        const newDirectionId = validAlternatives[Math.floor(Math.random() * validAlternatives.length)];
        this.currentDirection = this.directions.find(dir => dir.id === newDirectionId);
    }

 */



/* 
        this.directions = [
            { id: "right", vx: 1, vy: 0, alternatives: ["up-right", "down-right", "up", "down"] },
            { id: "down-right", vx: 1, vy: 1, alternatives: ["right", "down", "down-left", "left"] },
            { id: "down", vx: 0, vy: 1, alternatives: ["down-right", "down-left", "left", "right"] },
            { id: "down-left", vx: -1, vy: 1, alternatives: ["down", "left", "up-left", "up"] },
            { id: "left", vx: -1, vy: 0, alternatives: ["down-left", "up-left", "up", "down"] },
            { id: "up-left", vx: -1, vy: -1, alternatives: ["left", "up", "up-right", "right"] },
            { id: "up", vx: 0, vy: -1, alternatives: ["up-left", "up-right", "right", "left"] },
            { id: "up-right", vx: 1, vy: -1, alternatives: ["up", "right", "down-right", "down"] },
        ];
        this.currentDirection = this.directions[0]; // Start with "right" for example
     */



/* 
document.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'ArrowLeft':
            pacMan.moveLeft = true;
            break;
        case 'ArrowRight':
            pacMan.moveRight = true;
            break;
        case 'ArrowUp':
            pacMan.moveUp = true;
            break;
        case 'ArrowDown':
            pacMan.moveDown = true;
            break;
    }
});

// When the key is released this stops the movement of pacman. But shouldn't it always be moving ?
document.addEventListener('keyup', (event) => {
    switch (event.key) {
        case 'ArrowLeft':
            pacMan.moveLeft = false;
            break;
        case 'ArrowRight':
            pacMan.moveRight = false;
            break;
        case 'ArrowUp':
            pacMan.moveUp = false;
            break;
        case 'ArrowDown':
            pacMan.moveDown = false;
            break;
    }
});
 */

/* 

// ----------------- FRÁBÆR LEIÐ TIL AÐ PASSA UPPÁ AÐ OBJECT FARI EKKI ÚTFYRIR CANVAS ------ //
        // Bounce off walls by reversing velocity
        if (this.x <= 0 || this.x + this.width >= canvasWidth) {
            // Need to make every move of pacman false here
        }
        if (this.y <= 0 || this.y + this.height >= canvasHeight) {
            // Need to make every move of pacman false here
        }

 */

/* 
// Define the frame rate (e.g., 60 frames per second)
const frameRate = 60;
const frameDelay = 1000 / frameRate;
 */


/* 
    // Draw each dot
    dots.forEach(dot => dot.draw(ctx));
    console.log('drawDots function has been called')

 */


    /* 
    // Display "GAME OVER" message
    ctx.fillStyle = colors.blue; // Set text color
    ctx.font = '48px Arial'; // Set font size and family
    ctx.textAlign = 'center'; // Center the text
    ctx.fillText('GAME OVER', canvasWidth / 2, canvasHeight / 2); // In the middle
     */















/* <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Pac-Man Game</title>
    
    <style type="text/css">
        html, body {
            height: 100%;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        canvas {
            display: block;
        }
        
    </style>
</head>
<body>
    <canvas id="myPacManGame" style="border: 2px solid black; border-radius: 25px;"></canvas>
    <script src="minn_pacman.js"></script>
</body>
</html>

 */
        // Draw background that is transparent // not needed
/*         ctx.fillStyle = 'rgba(0, 0, 0, 0)';
        ctx.fillRect(this.x, this.y, this.width, this.height); */

// Start the game loop with the defined frame rate
/* setInterval(gameLoop, frameDelay); */
/* gameLoop(); */

/* 
for (let i = 0; i < 50; i++) {
    const x = Math.random() * (canvas.width - 2 * Dot.radius) + Dot.radius;
    const y = Math.random() * (canvas.height - 2 * Dot.radius) + Dot.radius;
    // const x = Math.random() * canvas.width;
    // const y = Math.random() * canvas.height;
    dots.push(new Dot(x, y));
}


 */
/* 

// Movement handling (to be expanded upon)
document.addEventListener('keydown', (e) = {
    // Handle the arrow keys for movement 
 });
 

 */

// This here would as expeced, fill up the entire window size
// canvas.width = window.innerWidth;
// canvas.height = window.innerHeight;

/* class Ghost {
    constructor(sprite, x, y, width, height, maxGhostSize) {
        this.sprite = sprite;
        this.x = x;
        this.y = y;
        this.width = Math.min(width, maxGhostSize);
        this.height = Math.min(height, maxGhostSize);
        this.maxGhostSize = maxGhostSize; // Add the new argument
    }

    // The function within the class to draw the ghost (easily callable)
    draw(ctx) {
        ctx.drawImage(
            this.sprite,
            this.x, 
            this.y, 
            this.width, 
            this.height,
            Math.random() * (ctx.canvas.width - this.width), // random x position
            Math.random() * (ctx.canvas.height - this.height), // Random y position
        )
    }
};
 */





/* 
function drawPacman() {
    // Pac-Man himself
    ctx.beginPath();
    ctx.arc(pacMan.x, pacMan.y, pacMan.radius, 0.2 * Math.PI, 1.8 * Math.PI);
    ctx.lineTo(pacMan.x, pacMan.y);
    ctx.fillStyle = pacMan.color;
    ctx.fill();
    ctx.closePath();
    
    // The Pac-Man eye
    ctx.beginPath();
    ctx.arc(pacMan.x + 5, pacMan.y - 10, 3, 0, 2 * Math.PI);
    ctx.fillStyle = colorBlack;
    ctx.fill();
    ctx.closePath();
};

 */







/* 




















/* 

function drawGhost(ctx) {
    
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

    ctx.fillStyle = colorWhite;
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

    ctx.fillStyle = colorBlack;
    ctx.beginPath();
    ctx.arc(101, 102, 2, 0, Math.PI * 2, true);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(89, 102, 2, 0, Math.PI * 2, true);
    ctx.fill();
}
 */







/* 
// The Game Loop !!!
function gameLoop() {
    updatePositions(pacMan); // Update Pac-Man's position
    // Update ghosts ---- MISSING
    drawGame(); // Re-draw the entire screen
    requestAnimationFrame(gameLoop);

}

 */


/* 
function updatePositions(character) {
    if (character.moveLeft) {
        character.x -= character.speed
    }

    // Hérna kemur meira movement directions og collision detections
}
 */



/* 
// A utility function to draw a rectangle with rounded corners.

function roundedRect(ctx, x, y, width, height, radius, fill) {
    ctx.beginPath();
    ctx.moveTo(x, y + radius);
    ctx.arcTo(x, y + height, x + radius, y + height, radius);
    ctx.arcTo(x + width, y + height, x + width, y + height - radius, radius);
    ctx.arcTo(x + width, y, x + width - radius, y, radius);
    ctx.arcTo(x, y, x, y + radius, radius);
    
    // This way i can choose if i want the rectangle to be filled or not
    if (fill) {
        ctx.fillStyle = colorDarkBlue;
        ctx.fill(); 
    }

    // ctx.fill();  // Fill the inside of the wall
    
    ctx.stroke(); // Stroke the outlines of the rectangle
}
function drawWalls() {
    // Wall number 1
    roundedRect(ctx, 50, 50, 100, 150, 5, true);
    // Wall number 2
    roundedRect(ctx, 200, 50, 100, 100, 5, true)
    // Wall number 3
    roundedRect(ctx, 350, 50, 50, 100, 5, true)
    // Wall number 4
    roundedRect(ctx, 450, 50, 100, 150, 5, true)


    // Wall number 5
    roundedRect(ctx, 50, 250, 100, 50, 5, true)
    // Wall number 6
    roundedRect(ctx, 450, 250, 100, 50, 5, true)
    
    
    // Wall number 7
    roundedRect(ctx, 50, 350, 100, 50, 5, true)
    // Wall number 8
    roundedRect(ctx, 200, 350, 100, 50, 5, true)
    // Wall number 9
    roundedRect(ctx, 350, 350, 50, 50, 5, true)
    // Wall number 10
    roundedRect(ctx, 450, 350, 100, 50, 5, true)


    // Wall number 11
    roundedRect(ctx, 50, 450, 100, 100, 5, true)
    // Wall number 12
    roundedRect(ctx, 200, 450, 50, 100, 5, true)

    // Wall number 13
    roundedRect(ctx, 300, 450, 100, 100, 5, true)
    // Wall number 14
    roundedRect(ctx, 450, 450, 100, 100, 5, true)

    // Wall for the ghosts
    roundedRect(ctx, 200, 200, 200, 100, 5, false)
         
}


 */




/* 
const gridRows = 12;
const gridCols = 12;
let gameGrid = Array.from({ length: gridRows }, () => Array(gridCols).fill(0));
 */


/* This function draws the dots from the array... I need to figure out a way to make them
random and not collide with any walls... */
/* function drawDots(ctx) {
    dots.forEach(dot => {
        ctx.fillStyle = colorYellow;
        ctx.beginPath();
        ctx.arc(dot.x, dot.y, dot.radius, 0, Math.PI * 2);
        ctx.fill();
    })
}
 */





// Then i just draw the grid (I'm only using this for the debugging of the game and for my own learning purposes)
/* function drawGrid() {
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            ctx.strokeRect(j * gridSize, i * gridSize, gridSize, gridSize);
        }
    }
} */



















