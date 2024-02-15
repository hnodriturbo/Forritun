        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */


import { canvasWidth, canvasHeight } from "./game.js";

class collisionManager {
    constructor(pacMan, ghosts, dots, entityManager) {
        this.pacMan = pacMan;
        this.ghosts = ghosts;
        this.dots = dots;
        this.entityManager = entityManager;

        this.lastDot = false;
    }

    reset() {
        for (const ghost of Object.values(this.ghosts)) {
            ghost.reset();
        }

    }
    checkAllCollisions() {
        const collidedGhost = this.checkGhostCollisions();
        if (collidedGhost) {
            return collidedGhost;
        }   
        else {
            this.checkDotCollisions();
            this.checkCanvasCollisions();
        }

    }

    checkGhostCollisions() {
        // If Pac-Man is invulnerable just return and skip collision checking
        if (this.pacMan.invulnerable) {
            return;
        }

        // Create variable to hold the collided ghost
        let collidedGhost = null;

        for (const ghost of Object.values(this.ghosts)) {
            // Geth the distance from pacman x and y to ghost x and y
            const dx = this.pacMan.x - (ghost.x + ghost.radius);
            const dy = this.pacMan.y - (ghost.y + ghost.radius);


            // Use Math.sqrt to calculate the distance
            const distance = Math.sqrt(dx * dx + dy * dy);


            // Adjustment cause of Pac-Man's mouth so the collision looks closer
            let adjustment = 0;
            if (
                (this.pacMan.direction === 'left' && dx > 0) ||
                (this.pacMan.direction === 'right' && dx < 0) ||
                (this.pacMan.direction === 'up' && dy > 0) ||
                (this.pacMan.direction === 'down' && dy < 0)
            ) {
                adjustment = -5;
            }

            // Finally here we check for the collision if distance is less then these 3 variables put together
            if (distance < this.pacMan.radius + ghost.radius + adjustment) {
                console.log(`Pac-Man had a collision with ${ghost.name} ghost!`);
                collidedGhost = ghost; // Set the collided ghost into the variable to return it
                break; // Exit the loop
            }
        }

        // Return the collided ghost, or null if no collision occurred
        return collidedGhost; 
    }


    // Method for check for dot collision and splice the dot and add point for eaten dot
    checkDotCollisions() {
        
        for (let i = this.dots.length - 1; i >= 0; i--) {
            let dx = this.pacMan.x - this.dots[i].x;
            let dy = this.pacMan.y - this.dots[i].y;
            
            // c í öðru = a í öðru PLÚS b í öðru
            let distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < this.pacMan.radius + this.dots[i].radius) {
                // Here is a collition detected, PacMan eats the dot           
                this.pacMan.eatDot();
                this.dots.splice(i, 1); // Remove the dot from the array
                if (this.dots.length == 0) {
                    this.lastDot = true;
                }
            }
        }
    }

    // Merge the checking of Pac-Man and ghosts canvas collision checking
    checkCanvasCollisions() {
        // Pac-Man canvas collision
        this.pacManCanvasCollision();

        // Use Object.values(this.ghosts).forEach to check each ghost for canvas collision
        Object.values(this.ghosts).forEach(ghost => {
            this.ghostCanvasCollision(ghost);
        });
    }


    // Method checking Pac-Man canvas collisions
    pacManCanvasCollision() {
        // When pacman x (his center) reaches the 25px then put x position of pacman there
        if (this.pacMan.x - this.pacMan.radius <= 0) {
            this.pacMan.x = this.pacMan.radius; 
        } 
        if (this.pacMan.x + this.pacMan.radius >= canvasWidth) { 
            this.pacMan.x = canvasWidth - this.pacMan.radius; 
        }
        if (this.pacMan.y - this.pacMan.radius <= 0) { 
            this.pacMan.y = this.pacMan.radius; 
        }
        if (this.pacMan.y + this.pacMan.radius >= canvasHeight) { 
            this.pacMan.y = canvasHeight - this.pacMan.radius; 
        }
    }
    ghostCanvasCollision(ghost) {
        // Detect collision with left or right canvas boundaries
        if (ghost.x <= 0) {
            ghost.setRandomDirection('left');
        } else if (ghost.x + ghost.width >= canvasWidth) {
            ghost.setRandomDirection('right');
        }
    
        // Detect collision with top or bottom canvas boundaries
        if (ghost.y <= 0) {
            ghost.setRandomDirection('top');
        } else if (ghost.y + ghost.height >= canvasHeight) {
            ghost.setRandomDirection('bottom');
        }
    }
    
    


}

export default collisionManager;

    
/* 
        Object.values(this.ghosts).forEach(ghost => {
            const dx = this.pacMan.x - (ghost.x + ghost.radius);
            const dy = this.pacMan.y - (ghost.y + ghost.radius);

            const distance = Math.sqrt(dx * dx + dy * dy);


                // Adjustment cause of Pac-Man's mouth so the collision looks closer
                let adjustment = 0;
                
                if (
                    (this.pacMan.direction === 'left' && dx > 0) ||
                    (this.pacMan.direction === 'right' && dx < 0) ||
                    (this.pacMan.direction === 'up' && dy > 0) ||
                    (this.pacMan.direction === 'down' && dy < 0)
                ) {
                    adjustment = mouthAdjustment;
                }


                if (distance < this.pacMan.radius + ghost.radius + adjustment) {
                    console.log(`Pac-Man had a collision with ${ghost.name} ghost!`);
                    this.entityManager.pacManDies();
                }
      
        });
 */

    

    
/* 
        // Ghosts collition
        Object.values(this.ghosts).forEach(ghost => {
            const collisionInfo = this.ghostCanvasCollision(ghost);
            if (collisionInfo.collided) {
                ghost.handleWallCollision(collisionInfo.wall)
            }
        });
 */



    

/* 

    ghostCanvasCollision(ghost) {
        let collided = false;
        let wall = null;
    
        // Check first for left or right wall collision
        if (ghost.x - ghost.radius <= 0 || ghost.x + ghost.radius >= canvasWidth) {
            collided = true;
            wall = ghost.vx > 0 ? 'right' : 'left';
        }
        // Check for top or bottom wall collision
        if (ghost.y - ghost.radius <= 0 || ghost.y + ghost.radius >= canvasHeight) {
            collided = true;
            wall = ghost.vy > 0 ? 'bottom' : 'top';
        }
    
        return { collided, wall };
    }
    
 */


