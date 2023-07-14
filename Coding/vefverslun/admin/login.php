<?php 
ob_start();
session_start();
/* ob_end_clean(); */
/* Error display */
/* 
ini_set('display_errors', 1);
error_reporting(E_ALL);
 */
/* Includa */
include "database.php";


/* Sækja villuskilaboð úr urlinu og setja inn í $error */
if(isset($_GET['error'])) {
    $error = $_GET['error'];
}

/* Ef ýtt er á post / submit takkann */
if($_SERVER["REQUEST_METHOD"] == "POST") {
    if(isset($_POST['username']) && isset($_POST['password'])) {
        $username = validate($_POST['username']);
        $password = validate($_POST['password']);
        }
        if(empty($username)) {
            header("Location: login.php?error=username is required");
            exit();
        }
        else if(empty($password)) {
            header("Location: login.php?error=password is required");
            exit();
        }

        if(checkIfUsernameExists($username)) {
            /* Fetch password */
            $hashedPassword = fetchHashFromDatabase($username);
            
            /* Validate the login credentials */
            if(validateLogin($username, $password)) {

                /* Sæki admin row með fetchAdmin og set í adminInfo */
                $adminInfo = fetchAdminInfo($username);

                /* Set session and cookies with admin_uid and login date */
                $_SESSION['admin_uid'] = $adminInfo['admin_uid'];

                $_SESSION['login_date'] = date("Y-m-d H:i:s");
                $cookie_expiry = time() + 3600; /* Ein klst er 3600 sek */

                /* Set cookies */
                setcookie('admin_uid', $adminInfo['admin_uid'], $cookie_expiry);
                setcookie('username', $username, $cookie_expiry);
                setcookie('name', $adminInfo['name'], $cookie_expiry);
                setcookie('login_date', $_SESSION['login_date'], $cookie_expiry);
                
                echo "<h1>You have been logged in</h1>";
                header("refresh:3;url=index.php");
                exit();
            } 
            else {
                /* Ef lykilorðið er ekki rétt */
                header("Location: login.php?error=Password you entered not correct");
                exit();
            }
        } 
        else {
            /* notendanafn er ekki til */
            header("Location: login.php?error=Notendanafn finnst ekki");
            exit();
        }


}
/* Validater */
function validate($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/* These methods are typically used when retrieving multiple columns
or when you need to bind and fetch values for further processing.    
$stmt->store_result();
$stmt->bind_result($passwordHash);
$stmt->fetch();
*/

/* Functionið sem sækir hashaða lykilorðið í database útfrá username */
function fetchHashFromDatabase($username) {
    global $conn;
    /* sql skipun */
    $sql = "SELECT password FROM admin_accounts WHERE username = ?";
    /* undirbúningur  */
    $stmt = $conn->prepare($sql);
    /* Læsi breytuna inn í statementið */
    $stmt->bind_param("s", $username);
    /* framkvæmi */
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();
    /* Hægt að skila með if clause eða or clause */
    $password = $row['password'] ?? null;
    return $password;
}  
function checkIfUsernameExists($username) {
    global $conn;
    /* Telja hvað mörg rows eru til með tiltekið username */
    $sql = "SELECT COUNT(*) FROM admin_accounts WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    /* geyma niðurstöðu (meira notað þegar fetchað er multiple rows) */
    $stmt->store_result();
    $stmt->bind_result($count);
    $stmt->fetch();
    $stmt->close();
    // If at least one row was found, return true; otherwise, return false
    return $count > 0;

}
/* Bera saman hashaða lykilorðið við innslegið lykilorðið */
function validateLogin($username, $password) {
    $passwordHash = fetchHashFromDatabase($username);
    /* Ef passwordHash skilar lykilorði frá gagnagrunn og pass_verify matchar þau þá return true */
    if($passwordHash && password_verify($password, $passwordHash)) {
        return true;
    }
    return false;
}
/* Sækja admin row úr database og setja info í array */
function fetchAdminInfo($username) {
    global $conn;

    $sql = "SELECT * FROM admin_accounts WHERE username = ?";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();

    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();
    $adminInfo = array(
        'admin_id' => $row['admin_id'] ?? null,
        'name' => $row['name'] ?? null,
        'email' => $row['email'] ?? null,
        'username' => $row['username'] ?? null,
        'admin_uid' => $row['admin_uid'] ?? null
    );
    return $adminInfo;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap icons -->
    <link href="img/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../../bootstrap/dist/css/bootstrap.min.css">
    <!-- Mitt eigið CSS -->
    <link rel='stylesheet' type='text/css' media='screen' href='css/sass.css'>
    <link rel='stylesheet' type='text/css' media='screen' href='css/mystyle.css'>

    <!-- Bootstrap og jquery -->
    <script src="js/bootstrap.bundle.js"></script>
    <script src="js/jquery.js"></script>
  
    <!-- Bý til font class -->
    <style>
      /* Font-face and custom-text styles */
      @font-face {
      font-family: 'kirstyRegularItalic';
      src: url('font/kirsty/kirsty_rg_it.otf') format('opentype');
      }
      @font-face {
      font-family: 'kirstyBoldItalic';
      src: url('font/kirsty/kirsty_bd_it.otf') format('opentype');
      }
      .kirsty-regular-italic {
      font-family: 'kirstyRegularItalic', sans-serif;
      }
      .kirsty-bold-italic {
      font-family: 'kirstyBoldItalic', sans-serif;
      }
      </style>
    <!-- Titill síðunnar -->
    <title>Admin - Crystal 3D Pictures</title>
</head>
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid kirsty-regular-italic">

        <!-- Row og col sem geymir Admin table -->
        <div class="row vh-100 justify-content-center align-items-center">

            <div class="col-lg-8 col-12">


                <div class="row">
                    <div class="col-12">
                        <!-- ----- FORM START ----- -->
                        <form action="login.php" method="POST" name="login">

                            <div class="card card-lg-width w-75">
                                <div class="card-header bg-dark-subtle center center-header mx-auto">
                                <h4 class="card-title text-center">Innskráning Admins</h4>
                                </div>

                                <div class="card-body">
                                    <!-- Row -->
                                    <div class="row p-3 align-items-center justify-content-center"> 
                                        <div class="col">
                                            <h1></h1>
                                        </div>
                                    </div>

                                    <!-- Línan -->
                                    <hr class="my-horizontal-line">

                                
                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">Username:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="text" name="username" placeholder="Please enter your username" aria-label="default input example" style="background-color: #F2F2F2;">
                                        </div>          
                                    </div>  
                                    <!-- Row og 2 cols -->
                                    <div class="row p-3 align-items-center"> 
                                        <div class="col-3">
                                            <label class="text-align" style="color: #CCCCCC;">Password:</label>
                                        </div>
                                        <div class="col-9" style="padding: 0;">
                                            <input class="form-control bg-dark-subtle" type="password" name="password" placeholder="Please enter your password" aria-label="default input example">
                                        </div>
                                    </div>

                                </div><!-- card-body -->

                                <div class="card-footer pb-5 d-flex justify-content-center">
                                <!-- update takkinn -->
                                <button class="btn btn-outline-secondary" type="submit" name="login" style="width: 50%;">Login</button>
                                </div>
                            </div>
                        </form>
                    </div><!-- col -->
                    
                </div><!-- row -->

                <!-- Hérna eru villuskilaboðin ef reitir eru tómir -->
                <?php if (isset($error)) : ?>
                    <div class="row justify-content-center">
                        <div class="col-8">
                            <div class="alert alert-danger center" role="alert">
                                <?php echo $error; ?>
                            </div>
                        </div>
                    </div>
                <?php endif; ?>
                

            </div> <!-- col-lg-8 col-12 d-lg-flex -->
        </div><!-- row -->
    </div><!-- container-fluid -->