<?php

    include "config.php";

    $sql = "SELECT * FROM `users`";

    $result = $conn->query($sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        <!-- Include Bootstrap CSS -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    
</head>
<body>
    <div class="container">
        <h2>users</h2>
        <table class="table">
            <head>
                <tr>
                    <th>ID</th>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>email</th>
                    <th>gender</th>
                    <th>action</th>
                </tr>
            </head>
            <tbody>
                <?php
                    if($result->num_rows>0) {
                        while($row = $result->fetch_assoc()) {
                ?>

                        <tr>
                            <td> <?php echo $row["id"]; ?></td>
                            <td> <?php echo $row["firstname"]; ?></td>
                            <td> <?php echo $row["lastname"]; ?></td>
                            <td> <?php echo $row["email"]; ?></td>
                            <td> <?php echo $row["gender"]; ?></td>

                            <!-- Hér koma tveir takkar edit og delete -->
                            <td> 

                                <a class="btn btn-info" href="update.php?id=<?php echo $row["id"];?>">
                                    Edit
                                </a>

                            &nbsp; <!-- &nbsp býr til bil milli takkanna -->

                                <a class="btn-danger" href="delete.php?id=<?php echo $row["id"];?>">
                                delete
                                </a>

                            </td>
                            
                        </tr>

                <?php   }
                    }
                ?>

            </tbody>
        </table>
    </div>
</body>
</html>