<?php 
session_start();
ob_start();

/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
include "database.php";
include "sidebar.php";
include "topnavbar.php";
/* Næ í úr urli */
$action = $_GET['action'];
$source = $_GET['source'];

if (isset($_GET['user_uid'])) {
    $user_uid = $_GET['user_uid'];
}

/* function sem fetchar user og setur í array */
function fetchUserInfo($user_uid) {
    /* Opna tengingu */
    global $conn;
    /* Bý til tómt array */
    $userInfo = array();
    /* Prepare the query */
    $sql = "SELECT * FROM users WHERE user_uid = ?";
    /* Prepare the statement */
    $stmt = $conn->prepare($sql);
    /* Check if the statement was prepared successfully */
    if (!$stmt) {
        echo "Error in preparing statement: " . $conn->error;
        return $userInfo; // Return an empty array on failure
    }
    /* Bind the parameters */
    $stmt->bind_param('s', $user_uid);
    /* Keyri stmt */
    if($stmt->execute()) {
        /* Sæki niðurstöðu með stmt og set í $result */
        $result = $stmt->get_result();
        // check if a row is returned
        if ($result->num_rows > 0) {
            /* Fetcha niðurstöðuna og set í $row */
            $row = $result->fetch_assoc();
            /* Geymi svo user info í array */
            $userInfo['firstname'] = $row['firstname'];
            $userInfo['lastname'] = $row['lastname'];
            $userInfo['email'] = $row['email'];
            $userInfo['username'] = $row['username'];
            $userInfo['password'] = $row['password'];
            $userInfo['address'] = $row['address'];
            $userInfo['address2'] = $row['address2'];
            $userInfo['postalcode'] = $row['postalcode'];
            $userInfo['city'] = $row['city'];
            $userInfo['country'] = $row['country'];
            $userInfo['other'] = $row['other'];
        } else {
            echo "sql execution failed: " . $stmt->error;
        }
    }
    /* Close the stmt */
    $stmt->close();
    /* Returna arrayinu með userInfo */
    return $userInfo;
}

/* ---------- UPDATE USER ------------ */
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if($action == 'edit' && $source == 'users' && isset($user_uid)) {
        updateUserInfo($user_uid);
        header("Location: users.php?message=User $username updated successfully");
    }
}
function updateUserInfo($user_uid) {
    global $conn;
    if(isset($_POST['update'])) {
        /* Ná í allt info í gegnum post */
        $firstname = $_POST['firstname'];
        $lastname = $_POST['lastname'];
        $email = $_POST["email"];
        $username = $_POST["username"]; 
        $password = $_POST["password"];
        $address = $_POST["address"];
        $address2 = $_POST["address2"];
        $postalcode = $_POST["postalcode"];
        $city = $_POST["city"];
        $country = $_POST["country"];
        $other = $_POST["other"];

        $sql = "UPDATE users SET firstname=?, lastname=?, email=?, username=?, password=?, address=?, address2=?, postalcode=?, city=?, country=?. other=?";

        $stmt = $conn->prepare($sql);
        $stmt->bind->param("sssssssssss", $firstname, $lastname, $email, $username, $password, $adddress, $address2, $postalcode, $city, $country, $other);

        if($stmt->execute()) {
            return true;
        } else {
            echo "sql query error: " . $stmt->error;
        }
    }
    $stmt->close();
}

/*----- Htmlið sem sýnir alla reitina og userInfo er value þeirra --------*/
if ($action == 'view' && $source == 'users' && isset($_GET['user_uid'])) {
    /* sækja user */
    $userInfo = fetchUserInfo($user_uid);
    echo '
<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container row og col-lg-8 sem breytist í col-12 á minni skjám -->
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-lg-9 col-12 d-lg-flex">
                <!-- Formið byrjar hérna og er utan um allt cardið -->
                <form action="useraction.php?action=edit&source=users&user_uid=' . $user_uid . '&confirm=confirm" method="POST" name=updateUser class="w-100">
                    <!-- Card sem fyllir upp í plássið (w-100) -->
                    <div class="card card-lg-width w-100" style="margin-top: 12vw;">
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill w-100 d-flex justify-content-center align-items-center center" style="font-size: 22px; cursor: default;">Edit User Profile</h4>
                        </div>
                        <div class="card-body">
                            <!-- Línan -->
                            <hr class="my-horizontal-line" style="color: blue;">
                            <!-- Row og 4 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Firstname:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="firstname" value="' . $userInfo['firstname'] . '" aria-label="default input example">  
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Username:</label>
                                </div>
                                <div class="col-5" style="padding: 0;"> 
                                    <input class="form-control bg-dark-subtle" type="text" name="username" value="' . $userInfo['username'] . '" aria-label="default input example" style="background-color: #F2F2F2;">
                                </div> 
                            </div> 
                            <!-- Row og 4 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Lastname:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="lastname" value="' . $userInfo['lastname'] . '" aria-label="default input example">  
                                </div>
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Password:</label>
                                </div>
                                <div class="col-5" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="password" name="password" value="' . $userInfo['password'] . '" aria-label="default input example">
                                </div>
                            </div>
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
                                </div>
                                <div class="col-11" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="email" value="' . $userInfo['email'] . '" aria-label="default input example">  
                                </div>
                            </div> 
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Address:</label>
                                </div>
                                <div class="col-6" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="address" value="' . $userInfo['address'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Address 2:</label>
                                </div>
                                <div class="col-4" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="address2" value="' . $userInfo['address2'] . '" aria-label="default input example">
                                </div>
                            </div>
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-1">
                                <label class="text-align" style="color: #CCCCCC;">Postal Code:</label>
                                </div>
                                <div class="col-2" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="postalcode" value="' . $userInfo['postalcode'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">City:</label>
                                </div>
                                <div class="col-4" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="city" value="' . $userInfo['city'] . '" aria-label="default input example">
                                </div>
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Country:</label>
                                </div>
                                <div class="col-3" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="country" value="' . $userInfo['country'] . '" aria-label="default input example">
                                </div>
                            </div>

                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center">
                                <div class="col-1">
                                    <label class="text-align" style="color: #CCCCCC;">Other:</label>
                                </div>
                                <div class="col-11" style="padding: 0;">
                                    <textarea class="form-control bg-dark-subtle" name="other" aria-label="textbox example" style="height: 5vw;">' . $userInfo['other'] . '</textarea>
                                </div>
                            </div>
                        </div><!-- card-body -->
                        <div class="card-footer pb-5 d-flex justify-content-center">
                        <!-- update takkinn -->
                        <button class="btn btn-outline-secondary" type="POST" name="update" style="width: 50%;">Update</button>
                        </div>
                    </div><!-- card card-lg-width w-100" style="margin-top: 12vw;" -->
                </form>
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->
    
    ';
}


/*----------- delete user --------*/
function deleteUser($user_uid) {
    global $conn;
    $userInfo = fetchUserInfo($user_uid);

    // Debug statement to check user_uid
    echo "Deleting user with user_uid: " . $user_uid . "<br>";

    $sql = "DELETE FROM users WHERE user_uid = ?";

    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        echo "error: " . $conn->error;
        return false;
    }
    $stmt->bind_param("s", $user_uid);

    if($stmt->execute()) {
        $stmt->close();
        echo "User deleted successfully<br>"; // Debug statement
        return true;
    } else {
        echo "error in executing the query: " . $stmt->error;
        return false;
    }
    $conn->close();
}

/* Ef ýtt er á confirm takkann */
if ($action == 'delete' && $source == 'users' && isset($_GET['user_uid']) && isset($_GET['confirm'])) {
    $user_uid = $_GET['user_uid'];
    if (deleteUser($user_uid)) {
        header("Location: users.php?message=User " . $userInfo['username'] . " has been deleted successfully");
    } else {
        /* header("Location: users.php?message=User was not deleted"); */
    }
    exit();
}
/* html card sem spyr um staðfestingu á hvort eigi að delete user */
if ($action == 'delete' && $source == 'users' && isset($_GET['user_uid'])) {
    $user_uid = $_GET['user_uid'];
    $userInfo = fetchUserInfo($user_uid);
    echo '
    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
    <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
        <!-- Container fyrir skipulag contents -->
        <div class="container-fluid">
            <!-- Row og col sem geymir Users table -->
            <div class="row vh-100">
                <div class="align-items-center justify-content-center center h-100 w-100 mx-auto">
                    <!-- Cardið fyrir Users table -->
                    <div class="card card-lg-width col-lg-10 col-12 mx-auto justify-content-center align-content-center" style="margin-top: 100px;">
    
                    <div class="card-header bg-dark-subtle borderradius">
                        <h4 class="card-title text-center">Are you sure you want to delete user ' . $userInfo['username'] . '?</h4>
                    </div>

                    <div class="card-body mx-auto">
                        <br><br><br><br>
                    </div><!-- card-body -->

                    <div class="card-footer pb-5 d-flex justify-content-center align-items-center" style="border-top: 0px;">
                        <div class="col-2">
                            <a class="btn btn-danger btn-lg borderradius" href="useraction.php?action=delete&source=users&user_uid=<?php echo $user_uid; ?>&confirm=confirm" style="width: 200px; height: 50px;">Delete</a>
                        </div>
                
                        <div class="col-2"></div>
                
                        <div class="col-3">
                            <a class="btn btn-secondary btn-lg borderradius" href="users.php" style="width: 200px; height: 50px;">Cancel</a> 
                        </div>
                    </div>

                </div> <!-- card -->
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->

    ';
}
?>