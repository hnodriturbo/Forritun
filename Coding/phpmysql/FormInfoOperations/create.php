<?php 

    include "config.php";

    if(isset($_POST["submit"])) {
        $first_name = $_POST["firstname"];
        $last_name = $_POST["lastname"];
        $email = $_POST["email"];
        $password = $_POST["password"];
        $gender = $_POST["gender"];
    }

    $sql = "INSERT INTO `users` (`firstname`, `lastname`, `email`, `password`, `gender`) VALUES ('$first_name','$last_name','$email','$password','$gender')";

    $result = $conn->query($sql);

    if($result == TRUE) {
        echo "Nýjar upplýsingar hafa verið gerðar";
    } else {
        echo "Villa: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Signup form</h2>

    <form action="" method="POST">
        <fieldset>
            <legend>Personal information:</legend>
            First name:<br>
            <input type="text" name="firstname">
            <br>
            Last name:<br>
            <input type="text" name="lastname">
            <br>
            Email:<br>
            <input type="email" name="email">
            <br>
            Password: <br>
            <input type="password" name="password">
            Gender:<br>
            <input type="radio" name="gender" value="male">male
            <input type="radio" name="gender" value="female">female
            <br>
            <br>
            <input type="submit" name="submit" value="submit">
        </fieldset>
    </form>

    <a href="update.php">Update</a>


</body>
</html>