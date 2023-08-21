          <!-- -------------------- ADMIN SÍÐAN --------------------- -->
        <!-- ------------------- HREIÐAR PÉTURSSON -------------------- -->
      <!-- -------------------------------------------------------------- -->
    <!-- --------------------------- MADE 2023 ---------------------------- -->
 

<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ob_start(); // Required for header("Location...")
session_start();
var_dump($_POST);
$base_url = "../";

if (!isset($_SESSION['requested_url'])) {
    $_SESSION['requested_url'] = $_SERVER['REQUEST_URI'];
}

// Redirect if not logged in
if (!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date']) ||
    (isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date'])) {
    header("Location: " . $base_url . "login/login.php?error=You need to be logged in to see this site");
    exit();
}

$is_ajax = (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest');

if (!$is_ajax) {
    include_once "$base_url" . "sidebar.php";
    include_once "$base_url" . "topnavbar.php";
}
if (isset($_GET['closed']) && $_GET['closed'] == 'true') {
    if (isset($_SESSION['step-1-data'])) {
        unset($_SESSION['step-1-data']);
    }
    if (isset($_SESSION['step-2-data'])) {
        unset($_SESSION['step-2-data']);
    }
}
$goBackButtonAttribute = '';
$goBackButtonText = '';
$proceedButtonAttribute = '';
$proceedButtonText = '';
$formSubmitValue = '';

$action = $_GET['action'] ?? $_POST['action'] ?? "";

if (!$is_ajax) {
    echo '
    <div class="col-xl-10 col-12 offset-xl-2 kirsty-regular-italic offset vh-100 margin-top">
        <div id="main-content-container">';
}



if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    switch ($action) {
        case 'go-to-index':
            include 'create_menu.php';
            break;
        case 'create-order-step-1':
            $goBackButtonAttribute = 'go-to-index';
            $goBackButtonText = 'Go Back To Index';
            $proceedButtonText = 'Proceed To Step 2';
            $proceedButtonAttribute = 'create-order-step-2';
            $formSubmitValue = 'step-1-data';
            include 'create_order_info.php';
            break; 
        case 'create-order-step-2':
            $goBackButtonAttribute = 'create-order-step-1';
            $goBackButtonText = 'Go Back To Step 1';
            $proceedButtonText = 'Proceed To Step 3';
            $proceedButtonAttribute = 'create-order-step-3';
            $formSubmitValue = 'step-2-data';
            include 'create_order_info.php';
            break;

        case 'create-order-step-3':
            $goBackButtonAttribute = 'create-order-step-2';
            $goBackButtonText = 'Go Back To Step 2';
            $proceedButtonText = 'Proceed To Step 4';
            $proceedButtonAttribute = 'create-order-step-4';
            $formSubmitValue = 'step-3-data';
            include 'create_order_items.php';
            break;
            
        default:
            if (!$is_ajax) {
                include 'create_menu.php';
            }
        }
} 

else if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    // Value of formSubmit - Value saying which step was submitted
    $formSubmitValue = $_POST['formSubmit'] ?? "";

    // Execute code based on the retrived $action variable
    switch ($action) {

        // ----- ----- create-order-step-1 ----- ----- //
        case 'create-order-step-1':

            include('create_order_info.php');
            break;
       
        
        // ------------------ STEP 2 ----------------- //
        // ----- ----- create-order-step-2 ----- ----- //
        case 'create-order-step-2':

            if (isset($_POST['formData'])) {
                if($formSubmitValue === 'step-1-data') {
                    // Parse the form data into an associative array
                    parse_str($_POST['formData'], $formDataArray);
                    $_SESSION["{$formSubmitValue}"] = $formDataArray;
                }

            }
            include('create_order_info.php');
            break;
        // ------------------ STEP 2 ----------------- //
        // ----- ----- create-order-step-2 ----- ----- //


        // ------------------ STEP 3 ----------------- //
        // ----- ----- create-order-step-3 ----- ----- //    
        case 'create-order-step-3':
            if (isset($_POST['formData'])) {
                if($formSubmitValue === 'step-2-data') {
                    // Parse the form data into an associative array
                    parse_str($_POST['formData'], $formDataArray);
                    $_SESSION["{$formSubmitValue}"] = $formDataArray;
                }

            }

            // Include the create_order_items view page
            include('create_order_items.php');
            break;

            // ------------------ STEP 3 ----------------- //
            // ----- ----- create-order-step-3 ----- ----- //   
        case 'create-order-step-4':
            break;

        case 'go-to-index':
            include 'create_menu.php';
            break;

        case 'create_product':
            break;

        case 'create_user':
            break;

        default:
            include 'create_menu.php';
            break;
    }
}



    
if (!$is_ajax) {
    echo '</div> <!-- main-content-container -->
    </div> <!-- col-lg-10 col-12 -->';
}

if (isset($_SESSION['step-1-data']) || isset($_SESSION['step-2-data'])) {
    echo "<script>";
    if (isset($_SESSION['step-1-data'])) {
        // CONSOLE LOG THE STEP-1-DATA
        foreach ($_SESSION['step-1-data'] as $key => $value) {
            echo "console.log('$key: $value');";
        } 
    } 
    if (isset($_SESSION['step-2-data'])) {
        // CONSOLE LOG THE STEP-2-DATA
        foreach ($_SESSION['step-2-data'] as $key => $value) {
            echo "console.log('$key: $value');";
        }
    }
    echo "</script>";
}

/* 
            // Þetta er til að tjekka hvort infoið sé í session
            if (isset($_SESSION['step-2-data'])) {
                echo "<script>";
                foreach ($_SESSION['step-1-data'] as $key => $value) {
                    echo "console.log('$key: $value');";
                }
                foreach ($_SESSION['step-2-data'] as $key => $value) {
                    echo "console.log('$key: $value');";
                }
                echo "</script>";
            }
             */
?>


