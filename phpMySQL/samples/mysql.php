
<?php
/* This method is used to execute an SQL query directly 
and returns a result set. It can be used for queries 
that do not require placeholders or bound parameters.
Here's an example: */
$sql = "SELECT * FROM users"; // set þessa skipun inn í breytu
// tengist mysql með conn->query($sql) og næ í allt frá users og set í breytu
$result = $conn->query($sql); // 
// Hérna næ ég í röð og set í breytu
$row = $result->fetch_assoc();

// Accessing the data
echo $row['name'];
echo $row['email'];
?>

<?php
/* In PHP, placeholders in SQL statements are typically represented by 
question marks (?) or named placeholders using colon prefix 
(:placeholder_name). These placeholders are then bound to specific 
values using prepared statements. */
$sql = "SELECT * FROM users WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->execute([$user_id]);
?>

<?php
/* This method is used to fetch a single row from the result 
set obtained from the query. It returns an associative
array where the keys correspond to column names. */
$row = $result->fetch_assoc();
?>

<?php
/* This method is used to execute a prepared statement with the provided 
parameter values. It replaces the placeholders in the prepared statement 
with the specified values and executes the query. */
$stmt->execute([$user_id]);
?>

<?php
/* This property provides information about any errors that occur 
during the execution of an SQL query. If an error occurs, the 
property will contain the error message.  */
if ($conn->error) {
    echo "Error: " . $conn->error;
}
?>
<?php
/* Binding multiple parameters: */
$sql = "INSERT INTO users (name, email) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->execute([$name, $email]);
?>

<?php
/* Fetching multiple rows: */
$sql = "SELECT * FROM users";
$stmt = $conn->prepare($sql);
$stmt->execute();
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>


<?php
/* Binding named parameters: */
$sql = "SELECT * FROM users WHERE name = :name AND email = :email";
$stmt = $conn->prepare($sql);
$stmt->execute([':name' => $name, ':email' => $email]);
?>

<?php
/* Getting the number of affected rows: */
$sql = "DELETE FROM users WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->execute([$user_id]);
$affected_rows = $stmt->rowCount();
?>

<?php
/* Fetching a single column value: */
$sql = "SELECT name FROM users WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->execute([$user_id]);
$name = $stmt->fetchColumn();
?>





<!-- Meira um fetch_assoc() -->
<?php
/* When you use the fetch_assoc() method in MySQLi and assign the result 
to the $row variable, it will contain one row of data from the result 
set at a time. Each time you call fetch_assoc(), it advances the 
internal pointer to the next row in the result set and returns an 
associative array representing that row. */

$sql = "SELECT * FROM users";
$result = $conn->query($sql);

while ($row = $result->fetch_assoc()) {
    // Access data for the current row
    echo "Name: " . $row["name"] . ", Email: " . $row["email"] . "<br>";
}
/* 
In this example, within the while loop, each iteration of fetch_assoc() 
fetches one row of data from the result set and assigns it to the $row 
variable. You can access the individual column values of the current row 
using the column names as keys in the associative array.

The loop will continue executing as long as there are more rows in the 
result set. Each iteration will fetch the next row and update the $row 
variable accordingly.

So, $row will contain the current row's data, and it will be overwritten 
with each iteration of the loop until all rows have been processed. */
?>