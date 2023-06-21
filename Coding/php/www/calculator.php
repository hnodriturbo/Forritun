<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
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

<form action="calculator.php" method="get">
    <input type="number" name="number1" value="<?php echo $number1; ?>">
    <br>
    <input type="number" name="number2" value="<?php echo $number2; ?>">
    <input type="submit">
</form>

<?php
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




</body>
</html>