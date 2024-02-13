        /* ########## Hreiðar Pétursson ########## */
        /*  ######## Javascript Áfanginn ########  */
        /*   ######### Skilaverkefni 2 #########   */
        /*    ########   Febrúar 2024   #######    */



/* -------------------------------------------------------------- */
/* ----- ----- ----- ----- -- Dot code -- ----- ----- ----- ----- */
/* -------------------------------------------------------------- */

class Dot {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.radius = 5; // This being the size of the dot
        this.color = "rgba(0, 0, 70, 1)";
    }

    // Make special function to draw the dot within the class
    draw(ctx) {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fill();
    }
}



export default Dot;
