<?php 

session_start();


if (!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date']) ) {
    header("Location: login.php?error=You need to be logged in to see this site.");
    exit();
}
else if (isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site.");
    exit();
}

// Rest of your code

include "database.php";
include "sidebar.php";
include "topnavbar.php";


function getAdminUsers() {
    global $conn;

    $stmt = $conn->prepare("SELECT * FROM admin_accounts LIMIT 10");

    $stmt->execute();

    $result = $stmt->get_result();

    while ($row = $result->fetch_assoc()) {
        $admin_id = $row['admin_id'];
        $admin_name = $row['name'];
        $admin_email = $row['email'];
        $admin_username = $row['username'];
        $admin_password = $row['password'];
        $admin_uid = $row['admin_uid'];

        echo "<tr>";
        echo "<td>$admin_id</td>";
        echo "<td>$admin_name</td>";
        echo "<td>$admin_email</td>";
        echo "<td>$admin_username</td>";
        echo "<td>$admin_password</td>";
        echo "<td>$admin_uid</td>";
        echo "</tr>";
    }
}
function getUsers() {
    global $conn;

    $stmt = $conn->prepare("SELECT * FROM users LIMIT 10");
    $stmt->execute();
    $result = $stmt->get_result();

    while($row = $result->fetch_assoc()) {
        $user_id = $row['user_id'];
        $firstname = $row['firstname'];
        $lastname = $row['lastname'];
        $email = $row['email'];
        $username = $row['username'];
        $password = $row['password'];
        $address = $row['address'];
        $address2 = $row['address2'];
        $postalcode = $row['postalcode'];
        $city = $row['city'];
        $country = $row['country'];
        $other = $row['other'];
        
        echo "<tr>";
        echo "<td>$user_id</td>";
        echo "<td>$firstname</td>";
        echo "<td>$lastname</td>";
        echo "<td>$email</td>";
        echo "<td>$username</td>";
        echo "<td>$address</td>";
        echo "<td>$address2</td>";
        echo "<td>$postalcode</td>";
        echo "<td>$city</td>";
        echo "<td>$country</td>";
        echo "<td>$other</td>";
        echo "</tr>";
    }
}
function getLogs() {
    global $conn;

    $stmt = $conn->prepare("SELECT * FROM logs LIMIT 10");

    $stmt->execute();

    $result = $stmt->get_result();

    while($row = $result->fetch_assoc()) {
        $logs_id = $row['logs_id'];
        $user_id = $row['user_id'];
        $action = $row['action'];
        $date = $row['date'];

        echo "<tr>";
        echo "<td>$logs_id</td>";
        echo "<td>$user_id</td>";
        echo "<td>$action</td>";
        echo "<td>$date</td>";
        echo "</tr>";
    }
}
function getProducts() {
    global $conn;
    /* undirbý tengingu */
    $stmt = $conn->prepare("SELECT * FROM products LIMIT 10");
    if (!$stmt) {
        echo "error in preparing the query: " . $conn->error;
        return;
    }
    /* executa queryið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }
    $result = $stmt->get_result();
    if($result->num_rows === 0) {
        echo "no rows found";
    }
    while($row = $result->fetch_assoc()) {
        $product_id = $row['product_id'];
        $image = $row['image'];
        $name = $row['name'];
        $description = $row['description'];
        $price = $row['price'];
        $category_id = $row['category_id'];

        echo "<tr>";
        echo "<td>$product_id</td>";
        echo "<td>$image</td>";
        echo "<td>$name</td>";
        echo "<td>$description</td>";
        echo "<td>$price</td>";
        echo "<td>$category_id</td>";
        echo "</tr>";
    }
}
?>


    <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
    <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
        <!-- Container fyrir skipulag contents -->
        <div class="container-fluid">

            <!-- Row og col sem geymir Users table -->
            <div class="row">
                <div class="d-flex align-items-center justify-content-center col-lg-10 col-12 mx-auto">

                    <!-- Cardið fyrir Users table -->
                    <div class="card card-lg-width" style="margin-top: 70px;">
                        
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Users List</h4>

                        </div>
                      
                        <div class="card-body">
                            <div class="table-responsive border">
                                <div class="mytable">
                                    <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                        <thead>
                                            <tr>
                                                <th scope="col">User id</th>
                                                <th scope="col">Firstname</th>
                                                <th scope="col">Lastname</th>
                                                <th scope="col">E-mail</th>
                                                <th scope="col">Username</th>
                                                <th scope="col">Address</th>
                                                <th scope="col">Address2</th>
                                                <th scope="col">Postalcode</th>
                                                <th scope="col">City</th>
                                                <th scope="col">Country</th>
                                                <th scope="col">Other</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <?php getUsers(); ?>
                                        </tbody>
                                    </table>
                                </div> <!-- mytable -->
                            </div> <!-- table-responsive -->
                        </div> <!-- card-body -->
                        <div class="card-footer pb-5 d-flex justify-content-end">
                            <a href="users.php">
                                <button type="button" class="btn btn-outline-secondary justify-content-center">Open Users List</button>
                            </a>
                        </div> <!-- card-footer -->
                        
                    </div> <!-- card -->

                </div><!-- d-flex align-items-center justify-content-center h-100 col-10 mx-auto -->
            </div><!-- row users table -->
        </div> <!-- container fluid -->
        
        <!-- container fyrir admin table og logs table -->
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-6 col-12">
                    <div class="card card-lg-width">
                    <div class="card-header">
                    <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Admin Users List</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border">
                            <div class="mytable">
                                <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                    <tr>
                                        <th scope="col">Admin ID</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Email</th>
                                        <th scope="col">Username</th>
                                        <th scope="col">Password</th>
                                        <th scope="col" class="nowrap">Admin UID</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <?php getAdminUsers(); ?>
                                    </tbody>
                                </table>
                                </div>
                            </div>
                        </div>
                        <div class="card-footer pb-5 d-flex justify-content-end">
                            <a class="btn btn-outline-secondary" href="admins.php">Open Admin Users</a>
                        <!-- <button type="button" class="btn btn-outline-secondary">Open Admin Users List</button> -->
                        </div>
                    </div>
                </div> <!-- col-6 admin users table -->

                <!-- Logs table -->
                <div class="col-lg-6 col-12">
                    <div class="card card-lg-width">
                        <div class="card-header">
                        <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius w-100">Logs</h4>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive border">
                                <div class="mytable">
                                    <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                        <thead>
                                        <tr>
                                            <th scope="col">Logs ID</th>
                                            <th scope="col">User ID</th>
                                            <th scope="col">Action</th>
                                            <th scope="col">Date</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <?php getLogs(); ?>
                                        </tbody>
                                    </table>
                                    </div>
                                </div>
                            </div>
                            <div class="card-footer pb-5 d-flex justify-content-end">
                            <a class="btn btn-outline-secondary" href="logs.php">Open Logs</a>
                            </div>
                        </div><!-- card-body -->
                    </div><!-- card card-lg-width -->
                </div> <!-- col-6 logs table -->
                
            </div><!-- row -->
        </div><!-- container fluid -->
            
        
    </div> <!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->
