<!-- Þessi síða er eign Hreiðars -->
<!-- Búið til þann 13 júli 2023 -->
    <!-- Products.php -->


<?php 
    include "database.php";
    include "sidebar.php";
    include "topnavbar.php";
    /* Functionið til að fetcha úr gagnagrunninum */
    function getAdminUsers() {
        global $conn;

        $stmt = $conn->prepare("SELECT * FROM admin_accounts");

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
            echo "<td>$admin_uid</td>";
            echo "<td><a class='btn btn-outline-secondary' href='updateadmins.php?admin_id=".$row['admin_id']."'>Edit</a></td>";
            echo "</tr>";
        }
    }

?>


 <!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
 <div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
        <!-- Container fyrir skipulag contents -->
        <div class="container-fluid" style="width: 80%;">

            <!-- Row og col sem geymir Admin table -->
            <div class="row">
                <div class="col-12">
                    <div class="card card-lg-width" style="margin-top: 70px;">
                        <div class="card-header bg-dark-subtle center center-header mx-auto">
                        <h4 class="card-title text-center">Admin Users List</h4>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <div class="mytable">
                                <table class="table-bordered table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                    <tr>
                                        <th scope="col">Admin ID</th>
                                        <th scope="col">Name</th>
                                        <th scope="col">Email</th>
                                        <th scope="col">Username</th>
                                        <th scope="col" class="nowrap">Admin UID</th>
                                        <th scope="col">Action</th>
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
                        </div>
                    </div>
                </div> <!-- col-12 admin users table -->
