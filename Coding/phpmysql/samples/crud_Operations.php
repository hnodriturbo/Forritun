<?php 

// CRUD operations:

// Create (C):
// Inserting a new user into the database
$name = "John Doe";
$email = "johndoe@example.com";

$sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";
$result = mysqli_query($conn, $sql);

if ($result) {
    echo "User created successfully";
} else {
    echo "Error creating user";
}

// Read (R)
// Fetching a user's information from the database
$userID = 1;

$sql = "SELECT * FROM users WHERE id = $userID";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    $user = mysqli_fetch_assoc($result);
    echo "User ID: " . $user['id'] . "<br>";
    echo "Name: " . $user['name'] . "<br>";
    echo "Email: " . $user['email'] . "<br>";
} else {
    echo "User not found";
}


// Update (U)
// Updating a user's email address in the database
$userID = 1;
$newEmail = "newemail@example.com";

$sql = "UPDATE users SET email = '$newEmail' WHERE id = $userID";
$result = mysqli_query($conn, $sql);

if ($result) {
    echo "User email updated successfully";
} else {
    echo "Error updating user email";
}


// Delete (D)
// Deleting a user from the database
$userID = 1;

$sql = "DELETE FROM users WHERE id = $userID";
$result = mysqli_query($conn, $sql);

if ($result) {
    echo "User deleted successfully";
} else {
    echo "Error deleting user";
}



?>