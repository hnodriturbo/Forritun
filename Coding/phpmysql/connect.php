
<?php
/* Connecting to the database:
In this example, the mysqli constructor is used to establish a 
connection to the MySQL database. If the connection fails, an 
error message is displayed. */
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>





<!-- Tengjast og framkvæma query -->
<?php

    if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["submit"])) {
        $conn = mysqli_connect("localhost", "root","8655", "registration") or die("Connection failed" .mysqli_connect_error());
        if(isset($_POST["name"]) && isset($_POST["email"]) && isset($_POST["phone"]) && isset($_POST["bgroup"])) {
            $name = $_POST["name"];
            $email = $_POST["email"];
            $phone = $_POST["phone"];
            $bgroup = $_POST["bgroup"];

            $sql = "INSERT INTO `users` (`name`, `email`, `phone`, `bgroup`) VALUES ('$name', '$email', '$phone', '$bgroup')";

            $query = mysqli_query($conn,$sql);
            if($query) {
                echo "Entry successful";
            } else {
                echo "Error : " . mysqli_error($conn);
            }
        }

    }

?>