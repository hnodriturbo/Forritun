<?php 
include "database.php"; 
include "header.php";

?>
<!-- ---------- Hér byrjar síðan ---------- -->


<!-- Container -->
<div class="container text-center flex-column" style="width:1000px" id="form-container">
    <!-- Hér byrjar formið -->
    <form action="login.php" method="post">
        <!-- Row -->
        <div class="row p-3 align-items-center justify-content-center"> 
            <div class="col">
                <h1>Innskráning</h1>
            </div>
        </div>
        <!-- Línan -->
        <hr class="my-horizontal-line">

        <!-- error catch -->
        <?php if(isset($_GET["error"])) { ?>
            <p class="error"> <?php echo $_GET["error"];?></p>
        <?php } ?>


        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Username:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="text" name="username" placeholder="stimplaðu inn notendanafn" aria-label="default input example" style="background-color: #F2F2F2;">
            </div>          
        </div>  
        <!-- Row og 2 cols -->
        <div class="row p-3 align-items-center"> 
            <div class="col-2">
                <label class="text-align" style="color: #CCCCCC;">Password:</label>
            </div>
            <div class="col-10" style="padding: 0;">
                <input class="form-control bg-dark-subtle" type="password" name="password" placeholder="lykilorð" aria-label="default input example">
            </div>
        </div>
        <!-- Auka row fyrir bil -->
        <div class="row align-items-center">
            <br>
        </div>
        <!-- Row með submit takkanum -->
        <div class="row align-items-center">
            <div class="col">
            <input class="btn btn-primary" name="submit" type="submit" value="Login" style="width: 350px">
            </div>
        </div>
    </form>

