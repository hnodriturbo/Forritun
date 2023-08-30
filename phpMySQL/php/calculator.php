<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


<!-- // ---- BASIC REIKNIVÉL MEÐ TVEIMUR INPUT REITUM ---- -->
<?php
if (isset($_GET["number1"])) {
    $number1 = $_GET["number1"];
} else {
    $number1 = '';
}

if (isset($_GET["number2"])) {
    $number2 = $_GET["number2"];
} else {
    $number2 = '';
}
?>
<!-- // ---- BASIC REIKNIVÉL MEÐ TVEIMUR INPUT REITUM ---- -->
<form action="calculator.php" method="get">
    <input type="number" name="number1" value="<?php echo $number1; ?>">
    <br>
    <input type="number" name="number2" value="<?php echo $number2; ?>">
    <input type="submit">
</form>

<?php

// ---- BASIC REIKNIVÉL MEÐ TVEIMUR INPUT REITUM ----
if (isset($_GET["number1"]) && isset($_GET["number2"])) {
    $number1 = $_GET["number1"];
    $number2 = $_GET["number2"];
    $svar = $number1 + $number2;
}
?>

<?php if (isset($svar)): ?>
    <br>
    Svar: <?php echo $svar; ?>
<?php endif; ?>

<br><br><br><br><br><br><br><br><br>

<!-- ------------------------------------------------------ -->

<!-- ----- AÐEINS BETRI REIKNIVÉL ----- -->

<!-- step="0.1" gerir möguleikan að hafa kommutölu í reitnum -->
<form action="calculator.php" method="post">
    Fyrsta tala: <input type="number" step="0.1" name="tala1"> <br>
    OP: <input type="text" name="op"> <br>
    Önnur tala: <input type="number" step="0.1" name="tala2"> <br>
    <input type="submit">
</form>

<?php
    if (isset($_POST["tala1"]) && isset($_POST["tala2"]) && isset($_POST["op"])) {
        $tala1 = $_POST["tala1"];
        $tala2 = $_POST["tala2"];
        $op = $_POST["op"];

        if ($op == "+") {
            echo $tala1 + $tala2;
        } elseif ($op == "-") {
            echo $tala1 - $tala2;
        } elseif ($op == "/") {
            echo $tala1 / $tala2;
        } elseif ($op == "*") {
            echo $tala1 * $tala2;
        } else {
            echo "Ekki rétt merki";
        }
    }
?>



<!-- ----- AÐEINS BETRI REIKNIVÉL ----- -->

</body>
</html>