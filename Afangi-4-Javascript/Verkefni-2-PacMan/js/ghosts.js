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

        this.ghostSpeed = 2; // Adjustable speed
        this.maxGhostSize = 50;


        // Generate random positions within canvas boundaries, ensuring at least 50px from edges
        this.x = this.setRandomPosition(); // X position on canvas
        this.y = this.setRandomPosition(); // Y position on canvas
        
        // Apply max size
        this.width = this.maxGhostSize; // Width to draw on canvas
        this.height = this.maxGhostSize; // Height to draw on canvas



        // Initialize velocities in a random direction
        this.vx = this.setRandomDirectionInTheBeginning();
        this.vy = this.setRandomDirectionInTheBeginning();

/* 
        // Updated simpler set random direction
        this.setRandomDirection(true);
 */
        // Radius for collition detection
        this.radius = 25; // Invisible circle radius for collision detection


    }
    reset() {
        // Reset speed to the initial value
        this.ghostSpeed = 2;
        this.maxGhostSize = 50;
        // Reset position if necessary
        this.x = this.setRandomPosition();
        this.y = this.setRandomPosition();

        // Apply max size
        this.width = this.maxGhostSize; // Width to draw on canvas
        this.height = this.maxGhostSize; // Height to draw on canvas

        // Reset direction/velocity
        this.vx = this.setRandomDirectionInTheBeginning();
        this.vy = this.setRandomDirectionInTheBeginning();

        this.radius = 25;
    }
    setRandomDirectionInTheBeginning() {
        return (Math.random() - 0.5) * this.ghostSpeed + 2;
    }

    // Method to make a number for positioning of the ghost within the canvas
    setRandomPosition() {
        const minDistanceFromEdge = 50;
        const range = canvasSize - 2 * minDistanceFromEdge;
        const position = Math.random() * range + minDistanceFromEdge;
        return Math.floor(position);
    }
    setRandomDirection(collisionSide) {
        let options = [];
    
        switch (collisionSide) {
            case 'left':
                options = [
                    { vx: this.ghostSpeed, vy: 0 }, // Right
                    { vx: this.ghostSpeed, vy: -this.ghostSpeed }, // 45° Right-Up
                    { vx: this.ghostSpeed, vy: this.ghostSpeed } // 45° Right-Down
                ];
                break;
            case 'right':
                options = [
                    { vx: -this.ghostSpeed, vy: 0 }, // Left
                    { vx: -this.ghostSpeed, vy: -this.ghostSpeed }, // 45° Left-Up
                    { vx: -this.ghostSpeed, vy: this.ghostSpeed } // 45° Left-Down
                ];
                break;
            case 'top':
                options = [
                    { vx: 0, vy: this.ghostSpeed }, // Down
                    { vx: this.ghostSpeed, vy: this.ghostSpeed }, // 45° Right-Down
                    { vx: -this.ghostSpeed, vy: this.ghostSpeed } // 45° Left-Down
                ];
                break;
            case 'bottom':
                options = [
                    { vx: 0, vy: -this.ghostSpeed }, // Up
                    { vx: this.ghostSpeed, vy: -this.ghostSpeed }, // 45° Right-Up
                    { vx: -this.ghostSpeed, vy: -this.ghostSpeed } // 45° Left-Up
                ];
                break;
            default:
                // No collision side provided; choose any direction
                options = [
                    { vx: this.ghostSpeed, vy: 0 }, // Right
                    { vx: -this.ghostSpeed, vy: 0 }, // Left
                    { vx: 0, vy: this.ghostSpeed }, // Down
                    { vx: 0, vy: -this.ghostSpeed } // Up
                ];
        }
    
        const choice = options[Math.floor(Math.random() * options.length)];
        this.vx = choice.vx;
        this.vy = choice.vy;
    }
    


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

