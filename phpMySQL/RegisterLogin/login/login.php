<?php 
/* Error display */
ini_set('display_errors', 1);
error_reporting(E_ALL);
/* Starta session */
session_start();
/* Gagnagrunnstenging */
include "database.php";

/* Validate - veit ekki alveg hvað þetta á að gera */
if(isset($_POST["username"]) && isset($_POST["password"])) {
    function validate($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
}
$username = validate($_POST["username"]);
$password = validate($_POST["password"]);



if(empty($username)) {
    header ("Location: index.php?error=Username is required");
    exit();
}
else if(empty($password)) {
    header("Location: index.php?error=Password is required");
    exit();
}

$sql = "SELECT * FROM `users` WHERE `username`='$username'";

$result = mysqli_query($conn, $sql);

if(mysqli_num_rows($result) > 0) {
    $row = mysqli_fetch_assoc($result);
    $hashedPassword = $row["password"]; // Retrieve hashed password from the database
    if (password_verify($password, $hashedPassword)) { // Compare hashed passwords
        echo "Logged in";
        $_SESSION["username"] = $row["username"];
        $_SESSION["id"] = $row["id"];
        header("Location: home.php");
        exit();
    }
    
    

} else {
    header("Location: index.php?error=Incorrect username or password");
    exit();
}


?>