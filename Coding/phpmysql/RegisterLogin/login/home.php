<?php 
include "header.php";
session_start();

if(isset($_SESSION["id"]) && isset($_SESSION["username"])) {
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <br><br><br><br>

    <h1 class="center">Hello, <?php echo $_SESSION["username"]; ?></h1>
    <a class="center" href="logout.php">logout</a>
</body>
</html>

<?php
} else {
    header("Location: index.php");
}
?>
