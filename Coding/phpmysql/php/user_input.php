<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<!-- ----- að include annað skjal ----- -->

<?php // include "skjal.html" ?>
<?php // include_once "skjal.html" ?>
<?php // include "skjal.php" ?>

<!-- Það er hægt að gera breytur í einu skjali og kalla á þær hér -->
<!-- including a file inherits the functions and varibles in the php file -->

<!-- Checkboxes -->
<form action="user_input.php" method="post">
    Apples: <input type="checkbox" name="fruits[]" value="apples"><br>
    Oranges: <input type="checkbox" name="fruits[]" value="oranges"><br>
    Pears: <input type="checkbox" name="fruits[]" value="pears"><br>
    <input type="submit">
</form>

<!-- Get the values of the checkboxes - multiple pieces of information -->
<?php
if (isset($_POST["fruits"])) {
    $fruits = $_POST["fruits"];
    foreach ($fruits as $fruit) {
        echo $fruit . "<br>";
    }
}
?>


<!-- Associative Arrays -->
<br>
Student:
<form action="user_input.php" method="post">
    <input type="text" name="student">
    <input type="submit">
</form>

<?php
    $grades = array("Jim"=>"A+", "Hreiðar"=>"A++", "Pétur"=>"B+");
    // echo $grades[$_POST["student"]];
?>
<?php
    if (isset($_POST["student"])) {
        echo $_POST['student']; echo ": ";
        $student = $grades[$_POST["student"]];
        echo $student;

    }
?>


<form action="user_input.php" method="get">
    Name: <input type="text" name="name">
    <input type="submit">
</form>
<?php
    if (isset($_GET["name"])) {
        echo $_GET['name'];
    } else {
        echo "Nafnið finnst ekki";
    }
    ?>
<?php if(isset($name)): ?>
    <br>
    Nafnið þitt er: <?php echo $_GET["name"] ?>
<?php endif; ?>




<br><br><br>
<?php
    if (isset($_GET["nafn"])) {
        $nafn = $_GET["nafn"];
        unset($_GET["nafn"]);
    } else {
        $nafn = '';
    }
    
    if (isset($_GET["aldur"])) {
        $aldur = $_GET["aldur"];
        unset($_GET["aldur"]);
    } else {
        $aldur = '';
    }
?>

<form action="user_input.php" method="get">
    Name: <input type="text" name="nafn" value="<?php echo $nafn; ?>">
    <br>
    Age: <input type="number" name="aldur" value="<?php echo $aldur; ?>">
    <input type="submit">
</form>
<br>

<?php if(isset($nafn) && isset($aldur)): ?>
    <br>
    Nafnið þitt er: <?php echo $nafn; ?>
    <br>
    Aldur þinn er: <?php echo $aldur; ?>
<?php endif; ?>


<!-- 
<script>
    // Reset the form fields when the page is loaded
    window.onload = function() {
        document.getElementById("myForm").reset();
    };
</script> 
-->
<br><br>


<!-- ---- HÉRNA ERU IF, ELSE IF, ELSE SKILYRÐI ---- -->
<?php 
    // eitt if skilyrði
    $skilyrdi1 = false;
    if ($skilyrdi1){
        echo "You are male";
    } else {
        echo "you are not male <br>";
    }
    // Bæði skilyrði þurfa vera sönn
    $skilyrdi2 = true;
    if ($skilyrdi1 && $skilyrdi2){
        echo "Skilyrði 1 og 2 eru sönn";
    } else if ($skilyrdi1 && !$skilyrdi2) {
        echo "Annað skilyrði <br>";
    } else {
        echo "Ef hvorugt skilyrði er satt þá prentast þetta <br>";
    }
    // || þjónar sem or.
    if ($skilyrdi1 || $skilyrdi2){
        echo "You are male";
    } else {
        echo "you are not male <br> <br> <br>";
    }   
?>
<br><br><br>
<?php
    function getMax($tala1, $tala2, $tala3) {
        
        // Fleiri merki = "!=" "==" "<=" ">=" "!!"
        if ($tala1 >= $tala2 && $tala1 >= $tala3) {
            return $tala1;
        } elseif ($tala2 >= $tala1 && $tala2 >= $tala3) {
            return $tala2;
        } else {
            return $tala3;
        }
    }
    $haedstatalan = getMax(34,56,45);

    echo $haedstatalan;

?>

<!-- ------ HÉRNA ER SWITCH ------- -->
<form action="user_input.php" method="post">
    Einkunn: <input type="text" name="einkunn">
    <input type="submit">
</form>
<?php
if (isset($_POST["einkunn"])) {
    $einkunn = $_POST["einkunn"];

    switch($einkunn) {
        case "A":
            echo "Þú fékkst hæðstu einkunn!";
            break;
        case "B":
            echo "Þú fékkst B í einkunn";
            break;
        case "C":
            echo "Þú fékkst C í einkunn";
            break;
        default:
            echo "Skrifaðir einkunn vitlaust";
    }
}
?>
<!-- ------- WHILE OG FOR LÚPPURNAR ------- -->

<?php

// while lúppan
$index = 1;
while($index <= 10){
    echo "$index <br>";
    $index++;
}

// for lúppan
for ($i = 1; $i <= 10; $i++) {
    echo "$i <br>";
}
// önnur útgáfa af for lúppu
$luckyNumbers = array(4, 8, 14, 16, 23, 42);
for ($i=0; $i < count($luckyNumbers); $i++) {
    echo "$luckyNumbers[$i] <br>";
}

?>

<br><br><br>

         
</body>
</html>