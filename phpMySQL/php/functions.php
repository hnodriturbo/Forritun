<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
function sayHi(){
    echo "Hello User";
}

sayHi();
echo "<br>";
// return
function cube($num){
    return $num * $num * $num;
}
echo cube(4);
echo "<br>";
$cuberesult = cube(14);

echo $cuberesult;
?>



</body>
</html>