<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);

/* Innleiði database tengingu */
include "database.php";
/* Innleiði header inná síðuna */
include "header.php";

$successMessage = "";
 
/* Ef smellt er á submit takkann */
if(isset($_POST["submit"])) {
    /* Bindi ég info úr reitunum í breytur */
    $username = $_POST["username"];
    $password = $_POST["password"];
    $name = $_POST["name"];
    $email = $_POST["email"];

    /* undirbý tengingu við gagnagrunn og undirbý gagnagrunnskipun til framkvæmdar í stmt breytu */
    $stmt = $conn->prepare("INSERT INTO `users` (`username`, `password`, `name`, `email`) VALUES (?, ?, ?, ?)");
    /* Bindi breyturnar við stmt breytuna - hvert "s" þýðir string */
    $stmt->bind_param("ssss", $username, $password, $name, $email);
    /* Framkvæmi skipun */
    $stmt->execute();
    if ($stmt) {
        $successMessage = "Tókst!";
    } else {
        echo "Villa: " . $conn->error;
    }
}
/* 
    if ($stmt) {
        echo '<script>document.getElementById("form-container").classList.add("hide-form");</script>';
    } else {
        die("Error: " . $stmt->error);
    } */

?>


<!-- ---------- Hér byrjar síðan ---------- -->


<!-- Container -->
<div class="container text-center flex-column" style="width:1000px" id="form-container">
    <!-- Hér byrjar formið -->
    <form action="" method="post">
        <!-- Row -->
        <div class="row p-3 align-items-center justify-content-center"> 
            <div class="col">
                <h1>Register</h1>
            </div>
        </div>
        <!-- Línan -->
        <hr class="my-horizontal-line">
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Username:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="username" placeholder="Veldu þér notendanafn" aria-label="default input example" style="background-color: #F2F2F2;">
            </div>          
        </div>  
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Password:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="password" name="password" placeholder="Veldu þér lykilorð" aria-label="default input example">
            </div>
        </div>
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Nafn:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="name" placeholder="Vinsamlegast sláðu inn nafn" aria-label="default input example">
            </div>
        </div>
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="email" placeholder="Vinsamlegast sláðu inn e-mailið þitt" aria-label="default input example">  
            </div>
        </div>  
        <!-- Auka row fyrir bil -->
        <div class="row align-items-center">
            <br>
        </div>
        <!-- Row með submit takkanum -->
        <div class="row align-items-center">
            <div class="col">
            <input class="btn btn-primary" name="submit" type="submit" value="Submit" style="width: 350px">
            </div>
        </div>
    </form>



<!-- Tókst skilaboðin -->

    <div class="row p-3 align-items-center" style="padding: 0;">
        <div class="col align-items-center" style="padding: 0;">
            <?php echo $successMessage; ?>
        </div>
    </div>
</div>

<!-- <div id="message" style="display: none;">Thank you for submitting!</div>
 -->

