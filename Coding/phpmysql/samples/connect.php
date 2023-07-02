
<!-- Tengjast database og skila villu ef tenging gengur ekki -->
<?php

/* Connecting to the database: */
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

/* The mysqli constructor is used to establish a connection to the MySQL database. */
$conn = new mysqli($servername, $username, $password, $dbname);

/* If the connection fails, an error message is displayed. */
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>


<!-- Ná í gögn eftir $username og skila  -->
<?php

$sql = "SELECT * FROM users WHERE username=$username";

$result = mysqli_query($conn,$sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "Name: " . $row["name"] . "Email: " . $row["email"];
    } 
    
}else {
    echo "No result found";
}

?>


<!-- Tengjast og Sækja gögn sem eru inn í POST og framkvæma query í sömu runu //  -->
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