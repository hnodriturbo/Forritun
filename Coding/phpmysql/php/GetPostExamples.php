
<!-- Sýnishorn af _GET aðferðinni -->
<?php
    if(isset($_GET["name"]) || isset($_GET["age"])) {
        echo "hi ". $_GET['name']. "<br/>";
        echo "your age is". $_GET['age']." years old";
        exit();
    }
?>
<html>
    <body>
        <form action = "<?php $_PHP_SELF ?>" method = "GET">
            Name: <input type="text" name = "name" />
            Age: <input type="text" name = "age" />
            <input type="submit" />
        </form>
    </body>
</html>

<!-- Sýnishorn af _POST aðferðinni -->
<?php
    if(isset($_POST["name"]) || isset($_POST["age"])) {
        echo "hi ". $_POST['name']. "<br/>";
        echo "your age is". $_POST['age']." years old";
        exit();
    }
?>
<html>
    <body>
        <form action = "<?php $_PHP_SELF ?>" method = "POST">
            Name: <input type="text" name = "name" />
            Age: <input type="text" name = "age" />
            <input type="submit" />
        </form>
    </body>
</html>

 <!-- Sýnishorn af REQUEST aðferðinni -->
 <?php
    if(isset($_REQUEST["name"]) || isset($_POST["age"])) {
        echo "hi ". $_REQUEST['name']. "<br/>";
        echo "your age is". $_REQUEST['age']." years old";
        exit();
    }
?>
<html>
    <body>
        <form action = "<?php $_PHP_SELF ?>" method = "POST">
            Name: <input type="text" name = "name" />
            Age: <input type="text" name = "age" />
            <input type="submit" />
        </form>
    </body>
</html>