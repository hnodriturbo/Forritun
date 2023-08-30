<?php 

    /* Innleiði database tengingu */
    include "database.php";
    /* Innleiði header inná síðuna */
    include "header.php";
    $successMessage = "";
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (empty($_POST["username"]) || empty($_POST["password"]) || empty($_POST["email"])) {
            exit("Values empty");
        }
    
        if($stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?")) {
            $stmt->bind_param("s", $_POST["username"]);
            $stmt->execute();
            $result = $stmt->get_result();

            if($result->num_rows > 0 ) {
                echo "Notendanafn er nú þegar til í gagnagrunninum, reyndu aftur";
            }
            else {
                if($stmt = $conn->prepare("INSERT INTO `users` (`username`, `password`, `email`) VALUES (?, ?, ?)")) {
                    $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
                    $stmt->bind_param("sss", $_POST["username"], $password, $_POST["email"]);
                    $stmt->execute();
                    // þessi villuskilaboð er mjög gott að nota
                    if ($stmt->error) {
                        echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
                    } else {
                        // Insertion was successful
                        $successMessage = "Það tókst að skrá þig";
                    }

                    
                }
                else {
                    echo "Einhver villa kom upp";
                }
            }
            $stmt->close();
        }
        else{
            echo "Það hefur komið upp einhver villa";
        }
        $conn->close();
    }
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