        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */


import { canvasSize } from "./game.js";

/* -------------------------------------------------------------- */
/* ----- ----- ----- ----- Ghosts Code -- ----- ----- ----- ----- */
/* -------------------------------------------------------------- */

class Ghost {
    constructor(name, sprite, sx, sy, sWidth, sHeight) {
        this.name = name;
        this.sprite = sprite; // Sprite Image
        this.sx = sx; // Source X on sprite sheet
        this.sy = sy; // Source Y on sprite sheet
        this.sWidth = sWidth; // Source width from sprite sheet
        this.sHeight = sHeight; // Source height from sprite sheet

        this.ghostSpeed = 10; // Adjustable speed
        this.maxGhostSize = 50;


        // Generate random positions within canvas boundaries, ensuring at least 50px from edges
        this.x = this.setRandomPosition(); // X position on canvas
        this.y = this.setRandomPosition(); // Y position on canvas
        
        // Apply max size
        this.width = this.maxGhostSize; // Width to draw on canvas
        this.height = this.maxGhostSize; // Height to draw on canvas

        // Initialize velocities in a random direction
        this.vx = this.setRandomDirection();
        this.vy = this.setRandomDirection();

        // Radius for collition detection
        this.radius = 25; // Invisible circle radius for collision detection


    }


    // Method to make a number for positioning of the ghost within the canvas
    setRandomPosition() {
        const minDistanceFromEdge = 50;
        const range = canvasSize - 2 * minDistanceFromEdge;
        const position = Math.random() * range + minDistanceFromEdge;
        return Math.floor(position);
    }

    setRandomDirection() {
        return (Math.random() - 0.5) * this.ghostSpeed;
    }


/* 
    // Method for setting a random direction of ghost
    setRandomDirection() {
        let angle = Math.random() * 2 * Math.PI; // Random angle in radians
        this.vx = Math.cos(angle) * this.ghostSpeed; // Vertical position number
        this.vy = Math.sin(angle) * this.ghostSpeed; // Horizontal position number
    }
 */
    // Method to draw the ghost
    draw(ctx) {
        ctx.drawImage(
            this.sprite,
            this.sx, this.sy, this.sWidth, this.sHeight, // Source location on sprite sheet
            this.x, this.y, this.width, this.height // Location and size of the ghost being drawn
        );
    }

    move() {
        this.x += this.vx;
        this.y += this.vy;
        /* console.log(this.x + ' and ' + this.y); */
    }

}

export default Ghost;

/* 
// Create the instances of each ghost
function initializeGhosts() {

}

 */