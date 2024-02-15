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

        // Necessary for when I make instance of collisionManager later
        this.collisionManager = null;
 
        // RequestId for Animation Frame
        this.requestId = null;

        // Game freezing flag - Stopping ghosts + pacman from moving
        this.gamePaused = false;
        
        // For when pacman wins
        this.pacManWinsFlag = false;

        // Initialization logic...
        this.boundHandleKeyDown = this.handleKeyDown.bind(this);
        this.boundRestartGame = this.restartGame.bind(this);

        // Load ghost sprites & start game
        this.loadSpritesAndStartGame();
        
        // Bind the gameLoop
        this.gameLoop = this.gameLoop.bind(this);

        // Initial call to the manageEventListeners
        this.manageEventListeners(true);

            
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

            /* this.manageEventListeners(true); */
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

    start() {
        // Cancel any existing animation frame requests
        if (this.requestId) {
            cancelAnimationFrame(this.requestId);
        }
        this.requestId = requestAnimationFrame(() => this.gameLoop());
        this.pacManFreePass(); // 6 second free pass at the beginning
        played++
    }
        


    updateGame() {

        this.entityManager.updateEntities(this.gamePaused);

        const collidedGhost = this.collisionManager.checkAllCollisions();
        if (collidedGhost) {
            this.pacManDies();
        }

        if (this.entityManager.pacMan.eatDot) {
            this.updateGameStats(played, wins, losses);
        }

        if (this.collisionManager.lastDot) {
            this.pacManWinsFlag = true;
            cancelAnimationFrame(this.requestId);
            this.pacManWins();
            
        }

    }

    gameLoop() {
        // Start by clearing the canvas
        this.clearCanvas();
        // Update game state
        this.updateGame();
        /* this.updateGameStats(); */
        // Request Animation Frame for smoother animation
        if (!this.pacManWinsFlag) {
            this.requestId = requestAnimationFrame(() => this.gameLoop());
        }
        
    }


    pacmanResetPosition() {
        this.entityManager.pacMan.x = canvasWidth / 2;
        this.entityManager.pacMan.y = canvasHeight / 2;
        this.entityManager.pacMan.direction = null;
    }
    



    // Clear the canvas
    clearCanvas() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.fillStyle = 'rgba(0, 100, 240, 0.2)'; // LightBlue color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }


    /* -------------------------------------------------------- */
    /* ----- ----- Pac-Man Winning & Losing methods ----- ----- */
    /* -------------------------------------------------------- */

    pacManWins() {
        if (!this.pacManWinsFlag) return; // Prevent loop
        
        // Increment the counter of wins
        wins++;
        console.log('incremented the wins counter')

        this.updateGameStats(played, wins, losses);
        
        // Cancel the animation frame
        cancelAnimationFrame(this.requestId);
        console.log('cancelled the animation frame ID: ' + this.requestId)
        
        // Clear the canvas
        this.clearCanvas();
        
        // Show win message by saying true to show and true to win
        this.toggleMessage(false, true);
    }

    pacManLoses() {

        // First increment the counter of losses
        losses++
        // Update game stats
        this.updateGameStats(played, wins, losses);

        // Cancel the animation frame just in case
        cancelAnimationFrame(this.requestId);
        // Clear the canvas
        this.clearCanvas();
        // Show lose message by saying true to show and false to win or lose
        this.toggleMessage(true, false);
    }





    pacManDies() {
        this.entityManager.pacMan.removelive();
        this.updateGameStats(played, wins, losses);
    

        // This stops the movements of ghosts and pacman
        this.gamePaused = true;
        // Make Pac-Man invulnerable
        this.entityManager.pacMan.invulnerable = true;
        // Make Pac-Man invisible
        this.entityManager.pacMan.visible = true;
    
        if (this.entityManager.pacMan.lives == 0) {
           this.pacManLoses();
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





    restartGame() {
        // Remove the existing event listeners
        this.manageEventListeners(false);

        // Reset entityManager, collisionManager, gamePaused
        this.entityManager.reset(); // Reset entities
        this.collisionManager.reset(); // Reset collision state
        this.gamePaused = false;
        this.pacManWinsFlag = false;
        this.toggleMessage(false, false)
        // Add the event listeners
        this.manageEventListeners(true);
        // Restart the game loop
        this.loadSpritesAndStartGame();
    }



    
    // Update counters
    updateGameStats(played, wins, losses) {
        const lives = this.entityManager.pacMan.lives;
        const score = this.entityManager.pacMan.score;
        document.getElementById('playedCount').textContent = `Played: ${played}`;
        document.getElementById('winCount').textContent = `Won: ${wins}`;
        document.getElementById('lossCount').textContent = `Lost: ${losses}`;
        document.getElementById('lives').textContent = `Lives: ${lives}`;
        document.getElementById('score').textContent = `Score: ${score}`;
    }


    // Toggle win message or game over message
    toggleMessage(gameOverMessageDisplay, youWinMessageDisplay) {

        const gameOverMessage = document.getElementById('gameOverMessage');
        const youWinMessage = document.getElementById('winMessage');
        const playAgain = document.getElementById('playAgainButton')

        if (gameOverMessageDisplay) {
            gameOverMessage.classList.remove('d-none');
            playAgain.classList.remove('d-none');
        }
        if (youWinMessageDisplay) {
            youWinMessage.classList.remove('d-none');
            playAgain.classList.remove('d-none');
        }
        
        if (!gameOverMessageDisplay && !youWinMessageDisplay) {
            gameOverMessage.classList.add('d-none');
            youWinMessage.classList.add('d-none');
            playAgain.classList.add('d-none');
        }

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

    manageEventListeners(shouldAdd) {
        const playAgainButton = document.getElementById('playAgainButton');

        if (shouldAdd) {
            document.addEventListener('keydown', this.boundHandleKeyDown);
            playAgainButton.addEventListener('click', this.boundRestartGame);
        } else {
            document.removeEventListener('keydown', this.boundHandleKeyDown);
            playAgainButton.removeEventListener('click', this.boundRestartGame);
        }
    }

}

document.addEventListener('DOMContentLoaded', () => {
    const game = new Game();
});
/* 
    // Setup Event Listeners    
    setupEventListeners() {
        // Remove existing 'click' event listener from 'playAgainButton' if it exists
        const playAgainButton = document.getElementById('playAgainButton');

        // playAgainButton.removeEventListener('click', this.playAgain());

        playAgainButton.addEventListener('click', this.playAgain());
        // Re-bind and add 'click' event listener to 'playAgainButton'

        
        // Properly manage 'keydown' event listener to avoid duplicates
        if (this.boundHandleKeyDown) {
            document.removeEventListener('keydown', this.boundHandleKeyDown);
        }
        this.boundHandleKeyDown = (event) => this.handleKeyDown(event);
        document.addEventListener('keydown', this.boundHandleKeyDown);
    }

    playAgain() {
        this.restartGame();
        this.toggleMessage(false, true); // Hide win message if shown
        this.toggleMessage(false, false); // Hide lose message if shown
    };

 */

/*     
    setupEventListeners() {
        document.getElementById('playAgainButton').addEventListener('click', () => {
            this.restartGame();
            this.toggleMessage(false, true); // Hide win message if shown
            this.toggleMessage(false, false); // Hide lose message if shown
        
        });
        document.addEventListener('keydown', (event) => this.handleKeyDown(event))
    }

 */


/* 
        const messageElement = document.getElementById(isWin ? 'winMessage' : 'gameOverMessage');
        const playAgainButton = document.getElementById('playAgainButton');
         */
/*         
        if (show) {
            messageElement.classList.remove('d-none');
            playAgainButton.classList.remove('d-none');
        }
        if (hide) {
            messageElement.classList.add('d-none');
            playAgainButton.classList.add('d-none');
        }

         */
/*         
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.fillStyle = 'rgba(0, 100, 240, 0.2)'; // LightBlue color
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height); 
*/

/* 
        this.gamePaused = true

        setTimeout(() => {
            this.gamePaused = false;
        }, 5000)
         */