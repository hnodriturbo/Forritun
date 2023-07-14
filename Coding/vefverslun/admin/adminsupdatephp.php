<?php 
$name = "";
$email = "";
$username = "";
$password = "";
$admin_uid = "";

/* Uppfæra database info */
if (isset($_GET['admin_id'])) {
    $admin_id = $_GET['admin_id'];

    if (isset($_POST["update"])) {
        if (empty($_POST["name"]) || empty($_POST["email"]) || empty($_POST["username"]) || empty($_POST["password"])) {
            exit("Values empty");
        } else {
            $name = $_POST["name"];
            $email = $_POST["email"];
            $username = $_POST["username"]; 
            $password = $_POST["password"];

            $sql = "UPDATE `admin_accounts` SET `name`=?, `email`=?, `username`=?, `password`=? WHERE `admin_id`=?";
        
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("ssssi", $name, $email, $username, $password, $admin_id);

            if ($stmt->execute()) {
                header("Location: admins.php");
            } else {
                echo "Error updating record: " . $stmt->error;
            }
        }
    }
} else {
    echo "admin_id er ekki í URL-inu";
}
?>