<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    

<!--        <form action="user_input.php" method="get">
        Name: <input type="text" name="name">
        <input type="submit">
       </form>

       
       // 
-->




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


<script>
    // Reset the form fields when the page is loaded
    window.onload = function() {
        document.getElementById("myForm").reset();
    };
</script>







         
</body>
</html>