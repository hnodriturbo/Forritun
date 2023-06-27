<?php
/* Connecting to the database:
In this example, the mysqli constructor is used to establish a 
connection to the MySQL database. If the connection fails, an 
error message is displayed. */
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
<?php 
/*/*  The mysqli_query() function in PHP is primarily used for executing SQL
queries in MySQL databases. It can be used for a wide range of SQL commands, 
including SELECT, UPDATE, INSERT, DELETE, and more. */

/* Here's an example of how you can use mysqli_query() for different types of 
SQL commands:

SELECT statement: */
$sql = "SELECT * FROM table_name";
$result = mysqli_query($conn, $sql);

/* UPDATE statement: */
$sql = "UPDATE table_name SET column1 = value1 WHERE condition";
$result = mysqli_query($conn, $sql);

/* INSERT statement: */
$sql = "INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3)";
$result = mysqli_query($conn, $sql);

/* DELETE statement: */
$sql = "DELETE FROM table_name WHERE condition";
$result = mysqli_query($conn, $sql);

/* 
In each case, mysqli_query() executes the SQL query specified in the $sql 
variable using the database connection $conn. The function returns a result 
object that can be used to fetch and manipulate the query results, depending 
on the type of query executed.

However, it's important to note that the code you provided is susceptible to 
SQL injection attacks. It's recommended to use prepared statements or 
parameterized queries to mitigate this security risk. */
?>

<?php
/* Executing a query and fetching data:
In this example, a SELECT query is executed using the query() method. 
The num_rows property is used to check if any rows are returned. The 
fetch_assoc() method is used inside a loop to fetch each row as an 
associative array. */
$sql = "SELECT * FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "Name: " . $row["name"] . ", Email: " . $row["email"] . "<br>";
    }
} else {
    echo "No results found.";
}
?>

<?php
/* Inserting data into a table:
In this example, an INSERT query is executed using the query() method 
to insert data into the users table. The query() method returns true 
if the query is executed successfully. Otherwise, an error message is 
displayed using the error property. */
$name = "John Doe";
$email = "johndoe@example.com";

$sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";

if ($conn->query($sql) === true) {
    echo "Record inserted successfully.";
} else {
    echo "Error: " . $conn->error;
}
?>

<?php
/* Updating data in a table:
In this example, an UPDATE query is executed using the query() method 
to update the email address of a user with a specific ID. The success 
or failure of the query is determined using the query() method and the 
error property. */
$newEmail = "newemail@example.com";
$userId = 1;

$sql = "UPDATE users SET email='$newEmail' WHERE id=$userId";

if ($conn->query($sql) === true) {
    echo "Record updated successfully.";
} else {
    echo "Error: " . $conn->error;
}
?>

<?php
/* Fetching a Single Row of Data:
In this example, a SELECT query is executed to fetch a single row from 
the users table based on a specific ID. The fetch_assoc() method is used 
to retrieve the row as an associative array. The retrieved data is then 
accessed using the column names. */
$sql = "SELECT * FROM users WHERE id = 1";
$result = $conn->query($sql);
$row = $result->fetch_assoc();

if ($row) {
    echo "Name: " . $row["name"] . ", Email: " . $row["email"];
} else {
    echo "No results found.";
}
?>

<?php
/* Deleting a Record:
In this example, an DELETE query is executed to delete a record from the 
users table based on a specific ID. The success or failure of the query is 
determined using the query() method and the error property. */
$sql = "DELETE FROM users WHERE id = 1";

if ($conn->query($sql) === true) {
    echo "Record deleted successfully.";
} else {
    echo "Error: " . $conn->error;
}
?>

<?php
/* Prepared Statement with Parameter Binding:
In this example, a prepared statement is used with placeholders (?) for 
the name and email fields. The bind_param() method is used to bind the 
provided values to the placeholders, and the execute() method is used to 
execute the prepared statement. The result is obtained using the get_result() 
method, and the retrieved rows are iterated through and displayed. */
$sql = "SELECT * FROM users WHERE name = ? AND email = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $name, $email);
$stmt->execute();
$result = $stmt->get_result();

while ($row = $result->fetch_assoc()) {
    echo "Name: " . $row["name"] . ", Email: " . $row["email"] . "<br>";
}
?>

<?php
/* Getting the Number of Affected Rows:
In this example, an UPDATE query is executed to update the status column 
of the users table. The affected_rows property is used to retrieve the 
number of rows affected by the last query. */
$sql = "UPDATE users SET status = 'inactive' WHERE last_login < '2022-01-01'";
$conn->query($sql);
$affectedRows = $conn->affected_rows;

echo "Number of affected rows: " . $affectedRows;
?>

<?php
/* Checking if a Table Exists:
In this example, a SHOW TABLES query is executed to check if a table with 
the given name exists in the database. The num_rows property is used to 
determine if any rows are returned. */
$tableName = "users";
$sql = "SHOW TABLES LIKE '$tableName'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "The table '$tableName' exists.";
} else {
    echo "The table '$tableName' does not exist.";
}
?>

<?php
/* Transaction Handling:
In this example, a transaction is used to group multiple queries and 
ensure that they are either all executed successfully or rolled back 
in case of an error. The autocommit(false) disables autocommit mode, 
and begin_transaction() starts the transaction. The queries are executed, 
and if no exceptions occur, commit() is called to commit the changes. If 
an exception occurs, rollback() is called to undo the changes made during 
the transaction. */
$conn->autocommit(false); // Disable autocommit

try {
    // Start a transaction
    $conn->begin_transaction();

    // Execute multiple queries
    $sql1 = "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')";
    $conn->query($sql1);

    $sql2 = "UPDATE users SET email = 'updated@example.com' WHERE id = 1";
    $conn->query($sql2);

    // Commit the transaction
    $conn->commit();
    
    echo "Transaction completed successfully.";
} catch (Exception $e) {
    // Rollback the transaction if an error occurs
    $conn->rollback();
    
    echo "Transaction failed: " . $e->getMessage();
}

$conn->autocommit(true); // Enable autocommit
?>