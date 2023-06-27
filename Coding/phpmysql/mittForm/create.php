<?php 
include "database.php";
if (isset($_POST["submit"])) {
    $name = $_POST["name"];
    $kt = $_POST["kt"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];
    $password = $_POST["password"];



    $sql = "INSERT INTO notendur (`name`, `kt`, `email`, `phone`, `password`) VALUES ('$name', '$kt', '$email', '$phone', '$password')";

    $result = mysqli_query($conn,$sql);

    if($result === TRUE) {
        echo "Það tókst að setja " . $name . " í gagnagrunninn";
    } else {
        echo "Það kom upp vill: " . $sql . "<br><br>" . $conn->error;
    }

}

$conn->close()


?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Include Bootstrap CSS -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.css"> 
    <title>Document</title>
</head>
<body>

    
<form action="" method="post">
    <div class="container">

        <div class="col-12"></div>
            <input type="text" name="name">
        </div>
        <div class="col-12">
            <input type="text" name="kt">
        </div>
        <div class="col-12">
            <input type="email" name="email">
        </div>
        <div class="col-12">
            <input type="text" name="phone">
        </div>
        <div class="col-12">
            <input type="password" name="password">
        </div>
    </div>
</form>
</body>
</html>