<?php 
    $dbname = 'mittForm';
    $servername = "localhost";
    $username = "root";
    $password = "8655";

    $conn = new mysqli($servername,$username,$password,$dbname);

    if($conn->connect_error) {
        die("Connection error" . $conn->connect_error);
    }
?>