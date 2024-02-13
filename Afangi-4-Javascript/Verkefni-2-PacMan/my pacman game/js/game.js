        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */



/* import { canvasWidth, canvasHeight } from './config.js';  */


// Set the Constants for the width and height
export const canvasWidth = 1000;
export const canvasHeight = 500;
export const canvasSize = 600;



import entityManager from './entityManager.js'; // Entity Manager file
import collisionManager from "./collisionManager.js"; // Collision Manager file

let played = 0;
let wins = 0;
let losses = 0;

class Game {
    constructor() {
        // Define canvas and context
        this.canvas = document.getElementById('myPacManGame');
        this.ctx = this.canvas.getContext('2d');
        
        // Set the canvas width and height
        this.canvas.width = canvasWidth;
        this.canvas.height = canvasHeight;

        // Create the entity manager
        this.entityManager = new entityManager(this.ctx, canvasWidth, canvasHeight);


        this.collisionManager = null;
 
        this.requestId = null;

        this.gamePaused = false;

        this.loadSpritesAndStartGame();
        this.setupEventListeners();
        this.gameLoop = this.gameLoop.bind(this);

  
            
    }

    loadSpritesAndStartGame() {
        const ghostSprites = new Image();
        ghostSprites.src = 'sprites/ghosts.png';

        ghostSprites.onload = () => {
            console.log("Ghost sprites loaded with dimensions: ", ghostSprites.width, ghostSprites.height);
            
            this.entityManager.createGhosts(ghostSprites);
            console.log("Successfully created ghosts with the ghost sprites"); // After initializing entityManager
            
            this.entityManager.createDots();
            console.log("Successfully finished creating the dots array holding all the instances");
            
            // Now when everything is ready, i can initialize the collisionManager to manage all collisions between entities
            this.initializeCollisionManager();

            console.log("Now the this.start() function will be executed.");
            this.start();
        };
    }


    initializeCollisionManager() {
        // Now because the ghosts and dots are initialized I can set up the collisionManager
        this.collisionManager = new collisionManager(
            this.entityManager.pacMan,
            this.entityManager.ghosts,
            this.entityManager.dots,
            this.entityManager
        );
    }


    setupEventListeners() {
        document.getElementById('playAgainButton').addEventListener('click', () => {
            this.restartGame();
            this.toggleMessage(false, true); // Hide win message if shown
            this.toggleMessage(false, false); // Hide lose message if shown
        
        });
        document.addEventListener('keydown', (event) => this.handleKeyDown(event))
    }


    handleKeyDown(event) {
        if (event.key === 'ArrowLeft') {
            this.entityManager.pacMan.direction = 'left';
        } else if (event.key === 'ArrowRight') {
            this.entityManager.pacMan.direction = 'right';
        } else if (event.key === 'ArrowUp') {
            this.entityManager.pacMan.direction = 'up';
        } else if (event.key === 'ArrowDown') {
            this.entityManager.pacMan.direction = 'down';
        }
    }
    

    start() {
        this.requestId = requestAnimationFrame(() => this.gameLoop());
        this.pacManFreePass(); // 6 second free pass at the beginning
        played++;
    }
        

    updateGame() {
        const collidedGhost = this.collisionManager.checkAllCollisions();
        if (collidedGhost) {
            this.pacManDies(collidedGhost);
        }
        this.entityManager.updateEntities(this.gamePaused); // Updates Pac-Man, ghosts and dots

        /* this.collisionManager.checkAllCollisions(); */ // This constantly checks for the collisions

    }
    
/* 
    updateGameStats(lives, score) {
        document.getElementById('lives').textContent = 'Lives: ' + lives;
        document.getElementById('score').textContent = 'Score: ' + score;
    }
 */

    clearCanvas() {
        // Clear the canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.fillStyle = 'rgba(0, 100, 240, 0.2)'; // LightBlue color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }

    gameLoop() {
        /* console.log('Entering game loop...');  */// Debug statement worked
        // Start by clearing the canvas
        this.clearCanvas();

        // Update game state
        this.updateGame();

        // Request Animation Framr for smoother animation
        this.requestId = requestAnimationFrame(this.gameLoop);
    }

    /* Er að vinna með event listeners, pacmanwins, pacmanloses, restartgame, updategamestats gefur villu, dots gefa ekki score, færa score yfir í game ? */


    // Restart game by creating a new instance of the game class
    restartGame() {
        new this.constructor();
    }


    pacmanResetPosition() {
        this.entityManager.pacMan.x = canvasWidth / 2;
        this.entityManager.pacMan.y = canvasHeight / 2;
        this.entityManager.pacMan.direction = null;
    }
    

    pacManWins() {
        // First increment the counter of wins
        wins++;
        // Cancel the animation frame
        cancelAnimationFrame(this.requestId);
        // Clear the canvas
        this.clearCanvas();
        // Show win message by saying true to show and true to win
        this.toggleMessage(true, true);

    }


    pacManLoses() {
        // First increment the counter of losses
        losses++
        // Cancel the animation frame
        cancelAnimationFrame(this.requestId);
        // Clear the canvas
        this.clearCanvas();
        // Show lose message by saying true to show and false to win or lose
        this.toggleMessage(true, false);
    }

    // Updating counters
    updateGameStats(played, wins, losses, lives, score) {
        document.getElementById('playedCount').textContent = `Played: ${played}`;
        document.getElementById('winCount').textContent = `Won: ${wins}`;
        document.getElementById('lossCount').textContent = `Lost: ${losses}`;
        document.getElementById('lives').textContent = `Lives: ${lives}`;
        document.getElementById('score').textContent = `Score: ${score}`;
    }


    // Toggle win message or game over message
    toggleMessage(show, isWin) {
        const messageElement = document.getElementById(isWin ? 'winMessage' : 'gameOverMessage');
        if (show) {
            messageElement.classList.remove('d-none');
        }
        else {
            messageElement.classList.add('d-none');
        }
    }

    pacManDies(collidedGhost) {
        console.log(`Pac-Man had a collision with ${collidedGhost.name} ghost!`);
        this.entityManager.pacMan.removelive();
        this.updateGameStats(this.entityManager.pacMan.lives, this.entityManager.pacMan.score);
    

        // This stops the movements of ghosts and pacman
        this.gamePaused = true;
        // Make Pac-Man invulnerable
        this.entityManager.pacMan.invulnerable = true;
        // Make Pac-Man invisible
        this.entityManager.pacMan.visible = true;
    
        if (this.entityManager.pacMan.lives == 0) {
           this.gameOver();
        }
    
        else {
            // Set this timeout to one second so the game is frozen for one second and then this code runs
            setTimeout(() => { // Freeze game for one second before running this code
                this.pacmanResetPosition();
    
                this.gamePaused = false; // Start the game in 1 second after pacmans death
                
                let blinkIntervalID = setInterval(() => {
                    this.entityManager.pacMan.visible = !this.entityManager.pacMan.visible;
                }, 400);
    
                // Stop blinking and make Pac-Man visible and vulnerable after again in 6 seconds
                setTimeout(() => {
    
                    clearInterval(blinkIntervalID); // Stop the other setInterval time
                    this.entityManager.pacMan.visible = true; // Ensure he is visible in case the blink interval ends at false
                    this.entityManager.pacMan.invulnerable = false; // End the invulnerability
    
                }, 6000)

            }, 1000) // Freeze everything for this timeout of 1 second
        }
    }

    pacManFreePass() {
        this.entityManager.pacMan.invulnerable = true;
        let blinkIntervalID = setInterval(() => {
            this.entityManager.pacMan.visible = !this.entityManager.pacMan.visible;
        }, 400);

        // The code inside setTimeout will run after the time specified. 6sec. Making Pac-Man visible and not invulnerable
        setTimeout(() => {
            clearInterval(blinkIntervalID); // use clear interval to stop setInterval
            this.entityManager.pacMan.visible = true;
            this.entityManager.pacMan.invulnerable = false; // End the protection
        }, 6000); // 6 seconds of invulnerability and blinking with 400ms apart comes to an end
    }


}

document.addEventListener('DOMContentLoaded', () => {
    const game = new Game();
});





/*         
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.fillStyle = 'rgba(0, 100, 240, 0.2)'; // LightBlue color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height); 
*/