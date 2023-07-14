<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $phrase = "Giraffe Academy";
        echo strtoupper($phrase);
        echo "<br>";
        echo strtolower($phrase);
        echo "<br>";
        echo $phrase[0];
        echo "<br>";
        echo $phrase[-1];
        echo "<br>";
        // Replace         _-------_      _____
        echo str_replace("ffe", "panda", $phrase);
        echo "<br>";
        // SubString - Tekur streng, byrjar á index 8 og velur 3 stafi
        echo substr($phrase, 8, 3);

    ?>


</body>
</html>