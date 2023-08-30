<?php 

    include "config.php";
    $result = false;

    if(isset($_POST["update"])) {
        $firstname = $_POST["firstname"];
        $lastname = $_POST["lastname"];
        $user_id = $_POST["id"];
        $email = $_POST["email"];
        $gender = $_POST["gender"];
        $password =$_POST["password"];
    
        // $sql ="UPDATE `users` SET `firstname` = '$firstname', `lastname`='$lastname',`email`='$email',`gender`='$gender',`password`='$password',`id`='$user_id' ";
/* 
        $sql = "UPDATE users SET firstname=?, lastname=?, email=?, gender=?, password=? WHERE id=?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("sssssi", $firstname, $lastname, $email, $gender, $password, $user_id);
        $stmt->execute();
 */
        /*         
        $sql = "UPDATE users SET firstname=?, lastname=?, email=?, gender=?, password=? WHERE id=?";
        $result = $conn->prepare($sql);
        $result->execute([$firstname, $lastname, $email, $gender, $password, $user_id]);
 */
/* 
        if($stmt == TRUE) {
            echo "Uppfært !";
        } else {
            echo "Villa: " . $stmt->error;
            // echo "Villa: " . $sql . "<br>" . $conn->error;
        }
    } */


        // set skipun inn í breytu
        $sql = "UPDATE users SET firstname='$firstname', lastname='$lastname', email='$email', gender='$gender', password='$password' WHERE id='$user_id'";
        // set tengingu við database og skiptun sem á að framkvæma í query 
        // og set það í breytu
        $result = mysqli_query($conn, $sql);

        if ($result) {
            echo "Updated!";
        } else {
            echo "Error: " . mysqli_error($conn);
    }
}


    if(isset($_GET['id'])) {
        $user_id = $_GET['id'];

        $sql = "SELECT * FROM users WHERE id='$user_id'";
        $result = mysqli_query($conn, $sql);
/* 
        $sql = "SELECT * FROM `users` WHERE `id`='$user_id'";

        $result = $conn->query($sql);
 */
/* 
        $sql = "SELECT * FROM users WHERE id=?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $user_id);
        $stmt->execute();
    
        $result = $stmt->get_result();
 */

        if($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                $firstname = $row['firstname'];
                $lastname = $row['lastname'];
                $email = $row['email'];
                $password = $row['password'];
                $gender = $row['gender'];
                $user_id = $row['id'];

            }
        ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>

    <h2>User Update Form</h2>
    <form action="" method="POST">
        <fieldset>
            <legend>Personal information:</legend>
            First name:<br>
            <input type="text" name="firstname" value="<?php echo $firstname; ?>">
            <br>
            Last name:<br>
            <input type="text" name="lastname" value="<?php echo $lastname; ?>">
            <br>
            Email:<br>
            <input type="email" name="email" value="<?php echo $email; ?>">
            <br>
            Password: <br>
            <input type="password" name="password" value="<?php echo $password; ?>">
            Gender:<br>
            <input type="radio" name="gender" value="male" <?php if($gender == 'male'){ echo "checked";} ?> > male
            <input type="radio" name="gender" value="female" <?php if($gender == 'female'){ echo "checked";} ?> > female
            <br>
            <br>
            <!-- id -->
            <input type="hidden" name="id" value="<?php echo $user_id; ?>">

            <input type="submit" name="update" value="update">
            
        </fieldset>
    </form>

    <a href="update.php?id=<?php echo $user_id; ?>">Update</a>


    </body>
    </html>


<?php
        } else{
            header("Location: view.php");
        }
        
    }
?>
