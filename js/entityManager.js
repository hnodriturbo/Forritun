        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */


import { canvasWidth, canvasHeight } from "./game.js";
import Ghost from "./ghosts.js";
import pacMan from "./pacman.js";
import Dot from "./dots.js";

class entityManager {
    constructor(ctx, canvasWidth, canvasHeight) {
        // Add context control
        this.ctx = ctx;

        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        // Create the object for the ghosts
        this.ghosts = {};
        // Array to hold the dot instances
        this.dots = []; 

        // Flag to indicate if ghosts and dots are initialized
        this.ghostsInitialized = false;
        this.dotsInitialized = false;

        /* this.lastDot = false; */

        // First initialize the pacman properties
        pacMan.initialize(canvasWidth, canvasHeight);
        this.pacMan = pacMan;
        console.log(pacMan)


        
    }

    // Method for resetting
    reset() {
        this.ghosts = {}; // Resets ghosts object
        this.dots = []; // Clears dots array
        console.log(this.dots)
        this.ghostsInitialized = false;
        this.dotsInitialized = false;
        this.pacMan = null;
        pacMan.initialize(this.canvasWidth, this.canvasHeight); // Reinitialize Pac-Man
        this.pacMan = pacMan;
        console.log(pacMan)
        this.pacMan.reset();
    }

    createGhosts(ghostSprites) {
        // Create Ghost Objects with positions from sprite sheet and sizes from sprite sheet
        this.ghosts['blinky'] = new Ghost("Blinky", ghostSprites, 45, 40, 160, 160);
        this.ghosts['pinky'] = new Ghost("Pinky", ghostSprites, 45, 420, 160, 160);
        this.ghosts['inky'] = new Ghost("Inky", ghostSprites, 445, 40, 160, 160);
        this.ghosts['clyde'] = new Ghost("Clyde", ghostSprites, 445, 420, 160, 160);
        
        this.ghostsInitialized = true;

        console.log('Created the ghosts instances:', this.ghostsInitialized, this.ghosts); 
    }

    

    // Function to prepare the dots, make the x and y and push it to the dots array
    createDots() {
        const radius = 5;
        for (let i = 0; i < 50; i++) {
            const x = Math.random() * (canvasWidth - 2 * radius) + radius;
            const y = Math.random() * (canvasHeight - 2 * radius) + radius;
            this.dots.push(new Dot(x, y));
        }
        this.dotsInitialized = true;  

        console.log('Prepared the dots to the array:', this.dotsInitialized, this.dots);
          
    }


    updateEntities(gamePaused) {
        this.drawGhosts(gamePaused);
        this.drawPacMan(gamePaused);
        this.drawDots();
    }



    /* ----- Muna að sækja gamePaused úr game.js ----- */

    drawGhosts(gamePaused) {
        Object.values(this.ghosts).forEach(ghost =>  {
            /* ghost.canvasCollisionDetection(); */
    
            if (!gamePaused) {
                ghost.move(); // Move ghost only if game is not paused when pac-man dies
            }
    
            /* ghost.move(); */ // Update ghost's position
            ghost.draw(this.ctx) // Draw the ghost
        });
    }


    drawPacMan(gamePaused) {
        // Update Pac-Man's position based on current direction
        /* pacMan.move(); */

        if (!gamePaused) {
            pacMan.move();
        }


        // After updating position and handling collisions, draw Pac-Man on the canvas
        pacMan.draw(this.ctx);
    }

    drawDots() {
        this.dots.forEach(dot => dot.draw(this.ctx));
    }


}


export default entityManager;


/*  || this.pacMan.invulnerable */