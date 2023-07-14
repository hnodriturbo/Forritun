<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);

include "database.php";
include "sidebar.php";
include "topnavbar.php";

$name = "";
$email = "";
$username = "";
$password = "";
$admin_uid = "";

/* Uppfæra database info */
if (isset($_GET['admin_id'])) {
    $admin_id = $_GET['admin_id'];

    if (isset($_POST["update"])) {

        $name = $_POST["name"];
        $email = $_POST["email"];
        $username = $_POST["username"]; 
        $password = $_POST["password"];

        $sql = "UPDATE admin_accounts SET name=?, email=?, username=?, password=? WHERE admin_id=?";
    
        $stmt = $conn->prepare($sql);

        $stmt->bind_param("ssssi", $name, $email, $username, $password, $admin_id);
        if(!$stmt->execute()) {
            echo "Villa kom upp: " . $stmt->errno . " - " . $stmt->error;
        } 
           
        }
    
} else {
    echo "admin_id er ekki í URL-inu";
}

/* Sækja upplýsingarnar um valinn notanda */
if (isset($_GET['admin_id'])) {
    $admin_id = $_GET["admin_id"];

    $sql = "SELECT * FROM admin_accounts WHERE admin_id=?";
    $stmt = $conn->prepare($sql);

    $stmt->bind_param("i", $admin_id);
    
    if ($stmt->execute()) {
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $gamlaname = $row['name'];
                $gamlaemail = $row['email'];
                $gamlausername = $row['username'];
                $gamlapassword = $row['password'];
                $admin_uid = $row['admin_uid'];
            }
        } else {
            echo "No record found";
        }
    } else {
        echo "Error executing query: " . $stmt->error;
    }
}
?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">

        <!-- Row og col sem geymir Admin table -->
        <div class="row justify-content-center">
            <div class="col-lg-6 col-12 d-lg-flex">

                
                    <div class="card card-lg-width" style="margin-top: 12vw;">

                        <div class="card-header bg-dark-subtle center center-header mx-auto">
                            
                        <h4 class="card-title text-center">Breyta <?php echo "$name"; ?></h4>
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
                            <form action="updateadmins.php?admin_id=<?php echo $_GET['admin_id']; ?>" method="POST" name="update">
                   

                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align" style="color: #CCCCCC;">Name:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="name" value="<?php echo $gamlaname; ?>" aria-label="default input example">  
                                </div>
                            </div>  
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align" style="color: #CCCCCC;">E-mail:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="email" value="<?php echo $gamlaemail; ?>" aria-label="default input example">  
                                </div>
                            </div>  
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align" style="color: #CCCCCC;">Username:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="text" name="username" value="<?php echo $gamlausername; ?>" aria-label="default input example" style="background-color: #F2F2F2;">
                                </div>          
                            </div>  
                            <!-- Row og 2 cols -->
                            <div class="row p-3 align-items-center"> 
                                <div class="col-3">
                                    <label class="text-align" style="color: #CCCCCC;">Password:</label>
                                </div>
                                <div class="col-9" style="padding: 0;">
                                    <input class="form-control bg-dark-subtle" type="password" name="password" value="<?php echo $gamlapassword; ?>" aria-label="default input example">
                                </div>
                            </div>

                        </div><!-- card-body -->
                
                        <div class="card-footer pb-5 d-flex justify-content-center">
                        <!-- update takkinn -->
                        <button class="btn btn-outline-secondary" type="POST" name="update" style="width: 50%;">Update</button>
                        </div>
                    </div>
                </form>
         
            </div> <!-- col-12 admin users table -->
        </div><!-- row -->
    </div><!-- container-fluid -->
</div> <!-- col-lg-10 col-12 -->
<br><br><br>


