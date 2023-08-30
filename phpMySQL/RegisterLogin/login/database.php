<?php 
    $dbname = 'registerlogin';
    $servername = "localhost";
    $user = "root";
    $pass = "8655";

    $conn = new mysqli($servername,$user,$pass,$dbname);

    if($conn->connect_error) {
        die("Connection error" . $conn->connect_error);
    }
?>