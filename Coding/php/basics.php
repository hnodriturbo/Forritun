<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Prufa</title>
</head>
<body>
    
    <?php

        $name = "George";
        $age = 35;

        echo("Hello World");

        echo "<h1> Hreiðar's Síða</h1>";
        echo "<hr>"; // Horizontal rule -- strik yfir síðuna
        echo "<p> This is my site </p> ";

        echo "There once was a man named $name <br>";
        $name = "Hreiðar";
        echo "and he didn't like to be named $name <br>";
        echo "<br><br>";
        echo "His age is $age";
        echo "<br>";

        $phrase = "To be or not to be";
        echo "<br>";
        $age = 30;
        $float = 30.5;

        $isMale = false;

        echo 4.57;
        echo "<br>";
        echo $phrase;

    ?>
    <br>
    <br>



    <?php
        // Array
        $friends = array("Hreiðar", "Gunnar", "Pétur");
        $friends[1] = "NýttValue";

        // Accessing and displaying array elements
        foreach ($friends as $friend) {
            echo "<b> $friend . </b><br>";
        }

        // Counting the number of elements in the array
        echo "Number of friends: " . count($friends);
    ?>




    <br>
    <br>
    <!-- post veldur því að upplýsingarnar koma ekki í urlinu -->
    <form action="basics.php" method="post">
        password: <input type="password" name="password" value="<?php echo $password; ?>"><br>
        <input type="submit">
    </form>
    <br>
    <br>

    <!-- sæki upplýsingarnar með post líka -->
    <?php if(isset($password)): ?>
    <br>
    <?php echo $_POST["password"] ?>
    <?php endif; ?>



</body>
</html>