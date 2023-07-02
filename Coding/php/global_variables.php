

<!-- ------------------ $_SERVER['PHP_SELF'] -------------------

By using $_SERVER['PHP_SELF'] as the value of the form action, the form will be submitted to the 
same PHP script that is currently executing. This allows you to process the form data and display 
the result on the same page.
 -->
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
    <!-- Form inputs go here -->
    <input type="text" name="username">
    <input type="submit" value="Submit">
</form>
<!-- 
It's important to note that $_SERVER['PHP_SELF'] can also be used by malicious users to perform 
certain attacks like cross-site scripting (XSS) or code injection. It's recommended to properly 
sanitize and validate any user input before using $_SERVER['PHP_SELF'] or any other user-supplied 
data in your application.

 -->








<!-- ---------------------- $_REQUEST --------------------------

$_REQUEST is a combined array that contains the contents of $_GET, $_POST, and $_COOKIE.
It retrieves data from all available sources: URL query parameters, form submissions, and cookies.
Use $_REQUEST when you want a convenient way to access data regardless of the request method or source.
However, it's generally recommended to use $_GET, $_POST, or $_COOKIE directly to avoid potential security risks and be more explicit about the data source.
Here are small examples demonstrating the usage of these variables:
 -->
<!-- // HTML form:  -->
<form action="page.php" method="post"><input type="text" name="username"></form>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username']; // Retrieves the submitted username
    echo "Welcome, $username!";
}
$name = $_REQUEST['name']; // Retrieves data from $_GET, $_POST, or $_COOKIE with the name "name"
$age = $_REQUEST['age']; // Retrieves data from $_GET, $_POST, or $_COOKIE with the name "age"
$_
?>





<?php
/* ------------------------------- $_ENV -------------------------

$_ENV is an associative array that contains variables passed to the current PHP script from the 
environment.
It retrieves information from system environment variables, which are set outside of the PHP script.
Environment variables store system-specific information such as server configurations, database 
credentials, or custom settings.

Use $_ENV to access and utilize environment variables in your PHP script.

Example: If you have an environment variable named DB_HOST set to "localhost", 
you can access it using $_ENV['DB_HOST'].
*/
$databaseHost = $_ENV['DB_HOST']; // Retrieves the value of the environment variable "DB_HOST"
?>








<?php
/* ------------------------------- $_FILES -------------------------

$_FILES is a multidimensional associative array that contains information about uploaded files.
It retrieves data from the files uploaded through an HTML form with enctype="multipart/form-data".

Use $_FILES to access file information such as name, type, size, and temporary location.
Example: Suppose you have an HTML form with <input type="file" name="image"> for uploading an image. 
You can access the uploaded file using $_FILES['image'].
*/
?>

<!-- // HTML form:  -->
<form action="upload.php" method="post" enctype="multipart/form-data">
<input type="file" name="image">
</form>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $file = $_FILES['image']; // Retrieves the uploaded file information
    $fileName = $file['name']; // Retrieves the original file name
    $fileType = $file['type']; // Retrieves the file type
    $fileSize = $file['size']; // Retrieves the file size in bytes
    $fileTemp = $file['tmp_name']; // Retrieves the temporary file location
    // Move the uploaded file to a permanent location or perform further processing
}
?>







<?php /* -------------------------------$_COOKIE and $_SESSION------------------------- */

/* $_COOKIE and $_SESSION are both superglobal variables in PHP used for handling data related to
 user sessions, but they serve different purposes.

$_COOKIE is an associative array that contains all the cookies sent by the client browser to the server.

Cookies are small pieces of data stored on the client's browser and are used to maintain state and 
remember information between different page requests.

The data stored in cookies can be accessed on the client-side as well as on the server-side.

Cookies have an expiration time and can be persistent (stored on the client's browser) or 
non-persistent (stored only for the duration of the session).

Cookies are typically used for tasks like remembering user preferences, tracking user behavior, and 
implementing features like "Remember Me" functionality. */
?>

<?php
/* 
$_SESSION is an associative array that stores session data on the server for each user session.

Session data is stored on the server and associated with a unique session ID that is usually stored 
in a cookie on the client-side.

The session ID is sent with each request, allowing the server to identify and retrieve the associated 
session data.

Session data is not accessible directly by the client browser; it is stored securely on the server.

Sessions are typically used to store sensitive user data, maintain user authentication, and track user 
activity throughout a browsing session.

Session data is temporary and will be destroyed after a certain period of inactivity or when the user 
closes the browser.
 */
?>
<?php
/* 
Use $_COOKIE when you need to store small amounts of non-sensitive data on the client-side, and you 
want the data to persist across different page requests or browser sessions.

Use $_SESSION when you need to store larger amounts of sensitive data securely on the server-side, 
and you want the data to be accessible only to the server and associated with a specific user session.

In many cases, you may use both $_COOKIE and $_SESSION together to leverage their respective advantages.

For example, you can store a session ID in a cookie ($_COOKIE) and use it to retrieve session data 
($_SESSION) on the server-side. This combination allows you to maintain user sessions securely while 
utilizing cookies for additional functionality or customization.
 */
?>
