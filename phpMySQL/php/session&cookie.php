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

Session data is temporary and will be destroyed after a certain period of inactivity or when the 
user closes the browser.
 */
?>

<!-- Sýnishorn að geyma user_id og email í $_SESSION og ná í það -->
<?php
session_start();
// Store the user information in the session
$_SESSION['user_id'] = $userIdFromMySQL;
$_SESSION['email'] = $emailFromMySQL;
?>
<?php
session_start();
// Access the user information from the session
$userId = $_SESSION['user_id'];
$email = $_SESSION['email'];
?>

<?php
$_SESSION['username'] = 'john'; /* Sets the value of the 'username' session variable to 'john'. */

$username = $_SESSION['username']; /* Retrieves 'username' and assigns it to the $username */

isset($_SESSION['username']); /* Checks if the 'username' session variable is set. */

unset($_SESSION['username']); /* Unsets or removes the 'username' session variable. */

$_SESSION['cart'] = []; /* Initializes an empty array as the value of the 'cart' session variable. */

$_SESSION['cart'][] = 'item1'; /* Adds 'item1' to the 'cart' session variable, which is an array. */

$_SESSION['count']++; /* Increments the value of the 'count' session variable by one. */




/* Functions using session_: */
session_start(); /* Starts a new or resumes an existing session. */

session_unset(); /* Unsets or removes all session variables. */

session_name('my_session'); /* Sets the name of the session. */

session_id('abc123'); /* Sets a specific session ID. */
session_id(); /* Returns the current session ID. */

session_regenerate_id(); /* Regenerates the session ID to improve session security. */

session_status(); /* Returns the current session status. */

session_destroy(); /* Destroys all data registered to the current session. */

session_save_path('/path/to/sessions'); /* Sets the save path for session files. */

session_write_close(); /* Writes session data and closes the session. */

session_abort(); /* Discards the current session and clears session data. */

session_gc(); /* Performs garbage collection on expired sessions. */

/* Sets the parameters for the session cookie. */
session_set_cookie_params(3600, '/', '.example.com', true, true); 
// Set the session cookie parameters
$cookieParams = session_get_cookie_params();
// Customize the parameters
$cookieParams['lifetime'] = 3600; // Cookie expires in 1 hour
$cookieParams['path'] = '/'; // Cookie is available across the entire domain
$cookieParams['secure'] = true; // Cookie is only transmitted over HTTPS
$cookieParams['httponly'] = true; // Cookie is accessible only through HTTP
// Set the modified cookie parameters
session_set_cookie_params($cookieParams['lifetime'], $cookieParams['path'], $cookieParams['domain'], $cookieParams['secure'], $cookieParams['httponly']);
?>



<?php
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

