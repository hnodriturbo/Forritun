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