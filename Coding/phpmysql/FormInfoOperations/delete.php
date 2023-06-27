<?php
include "config.php";

if(isset($_GET['id'])) {
    $user_id = $_GET['id'];

    $sql = "DELETE FROM `users` WHERE `id`='$user_id'";
    $result = $conn->query($sql);
    if ($result == TRUE) {
        echo "Tókst að eyða út úr gagnasafni";
    } else {
        echo "Villa: " . $sql . "<br>" . $conn->error;
    }
}
header("location: view.php")
?>