        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */



/* -------------------------------------------------------------- */
/* ----- ----- ----- ----- Pac - Man code ----- ----- ----- ----- */
/* -------------------------------------------------------------- */

const pacMan = {

    // Initial properties of pacMan
    initialize: function(canvasWidth, canvasHeight) {
        // Starting positions of x and y to be center of the canvas and set radius to 25
        this.x = canvasWidth / 2,
        this.y = canvasHeight / 2,
        this.radius = 25,

        // Color from the color object holder
        this.color = "rgba(255, 255, 0, 1)",

        // Lives, speed and score
        this.lives = 3,
        this.speed = 2,
        this.score = 0,

        // Extras
        this.invulnerable = false,
        this.visible = true,

        // Begins stopped, but when a direction button is pressed, he goes on and don't stop. (Just like in the real game)
        this.direction = null


    },
    reset() {
        this.lives = 3;
        this.speed = 2;
        this.score = 0;
        this.visible = true;
    },


    move() {
        switch (this.direction) {
            case 'left':
                this.x -= this.speed;
                break;
            case 'right':
                this.x += this.speed;
                break;
            case 'up':
                this.y -= this.speed;
                break;
            case 'down':
                this.y += this.speed;
                break;
        }
    },




    eatDot() {
        this.score += 1; // Score goes up one point each time eatDot method is called
    },    

    removelive() {
        this.lives -= 1;
    },


            /* ----------------------------------------- */
            /* ----- Drawing part of Pac-Man class ----- */
            /* ----------------------------------------- */

    // Method for returning the startAngle, endAngle, eyeX and eyeY positions to draw from
    decideWhichWay() {
        let startAngle, endAngle; // variables for the mouth positions
        let eyeX, eyeY; // Variables for the eye positions

        // Pacman faces to his correct direction
        switch (this.direction) {
            case 'up':
                startAngle = 1.7 * Math.PI;
                endAngle = 1.3 * Math.PI;
                eyeX = this.x - 10; // Move eye left within the circle
                eyeY = this.y - 5; // Move eye upwards within the circle
                break;
            case 'down':
                startAngle = 0.7 * Math.PI; // Mouth opening downwards
                endAngle = 0.3 * Math.PI;
                eyeX = this.x + 10; // Move eye right within the circle
                eyeY = this.y + 5; // Move eye downwards within the circle
                break;
            case 'left':
                startAngle = 1.20 * Math.PI; // Mouth opening to the left
                endAngle = 0.80 * Math.PI;
                eyeX = this.x - 5; // Move eye further left within the circle
                eyeY = this.y - 10; // Also, move eye upwards within the circle
                break;
            case 'right':
                startAngle = 0.2 * Math.PI; // Mouth opening to the right
                endAngle = 1.8 * Math.PI;
                eyeX = this.x + 5; // Move eye right within the circle
                eyeY = this.y - 10; // Move eye upwards within the circle
                break;
            default:
                startAngle = 0.2 * Math.PI; // Mouth opening to the right
                endAngle = 1.8 * Math.PI;
                eyeX = this.x + 5; // Move eye right within the circle
                eyeY = this.y - 10; // Move eye upwards within the circle
                break;
        }
        return { startAngle, endAngle, eyeX, eyeY };
    },

    draw(ctx) {
        if (!this.visible) return; // Do not draw if Pac-Man is not visible
        // Begin to know which way he is going and where to start the drawing
        const { startAngle, endAngle, eyeX, eyeY } = this.decideWhichWay();

        // Pac-Man body
        ctx.beginPath();
        ctx.arc(pacMan.x, pacMan.y, pacMan.radius, startAngle, endAngle);
        ctx.lineTo(pacMan.x, pacMan.y);
        ctx.fillStyle = pacMan.color;
        ctx.fill();
        ctx.closePath();
        
        // The Pac-Man eye
        ctx.beginPath();
        ctx.arc(eyeX, eyeY, 3, 0, 2 * Math.PI);
        ctx.fillStyle = "rgba(0, 0, 0, 1)";
        ctx.fill();
        ctx.closePath();
    }
};

export default pacMan;