<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);
/* starta session og header virkar ekki nema hafa ob_start */
ob_start();
session_start();
/* Athuga hvort viðkomandi sé loggaður inn og redirecta í samræmi við það */
if(!isset($_SESSION['admin_uid']) || !isset($_SESSION['login_date'])) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
else if(isset($_COOKIE['admin_uid']) && time() > $_COOKIE['login_date']) {
    header("Location: login.php?error=You need to be logged in to see this site");
    exit();
}
/* includa og bý til síðu */
include "database.php";
include "sidebar.php";
include "topnavbar.php";

/* ---------- GET PAGINATED ORDERS ---------- */
function getPaginatedOrders($page, $perPage) {
    global $conn;
    /* Offset is how many rows to skip before fetching rows */
    $offset = ($page - 1) * $perPage;
    /* Prepare the stmt */
    $stmt = $conn->prepare("SELECT * FROM orders LIMIT ?, ?");
    if(!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    /* Bind the parameters */
    $stmt->bind_param('ii', $offset, $perPage);
    /* Execute the statement */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
    }
    /* fetch the result */
    $result = $stmt->get_result();
    /* Check for returned rows */
    if($result->num_rows === 0) {
        echo "no rows returned";
    }
    /* Loop through the result */
    while($row = $result->fetch_assoc()) {
        /* reyni displaya eins fáa colums og hægt er - FOR READABILITY */
        $order_id = $row['order_id'];
        $order_unique_id = $row['order_unique_id'];
        $user_id = $row['user_id'];
        $firstname = $row['firstname'];
        $lastname = $row['lastname'];
        $email = $row['email'];
        $address =$row['address'];
        $address2 =$row['address2'];
        $postalcode =$row['postalcode'];
        $city =$row['city'];
        $state =$row['state'];
        $country =$row['country'];
        $created_at =$row['created_at'];
        $final_price =$row['final_price'];

        echo "<tr>";
        echo "<td>$order_unique_id</td>";
        echo "<td>$user_id</td>";
        echo "<td>$firstname</td>";
        echo "<td>$email</td>";
        echo "<td>$address</td>";
        echo "<td>$city</td>";
        echo "<td>$country</td>";
        echo "<td>$$created_at</td>";
        echo "<td>$final_price</td>";
        echo "<td> <a class='btn btn-secondary custom-btn' href='orders_action.php?source=orders&order_unique_id=" . $order_unique_id . "&action=view'> View </a> </td>";
        echo "<td> <a class='btn btn-danger custom-btn' href='orders_action.php?source=orders&order_unique_id=" . $order_unique_id . "&action=delete'> Delete </a> </td>";
        echo "</tr>";
    }
}
/* count orders to know how many pages to display */
function countOrders() {
    global $conn;
    $sql = "SELECT count(*) FROM orders";
    $stmt = $conn->prepare($sql);
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    $count = $row[0];
    return $count;
}



?>
<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 16px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row">
            <div class="center">
               <!-- Cardið fyrir Users table -->
                <div class="card card-lg-width col-lg-10 col-12 mx-auto" style="margin-top: 100px;">
                    <div class="card-header d-flex justify-content-center">
                    <span class="alert alert-success rounded-pill minnborderradius center kirsty-bold-italic" style="width: 95%; font-size: 36px;">List Of Your Orders</span>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col">Order Unique ID</th>
                                            <th scope="col">User ID</th>
                                            <th scope="col">Firstname</th>
                                            <th scope="col">E-mail</th>
                                            <th scope="col">Address</th>
                                            <th scope="col">City</th>
                                            <th scope="col">Country</th>
                                            <th scope="col">Created At</th>
                                            <th scope="col">Final Price</th>
                                            <th scope="col" class="orders-action-column">Action</th>
                                            <th scope="col" class="orders-action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <?php 
                                        /* Check if the page is set in the url. Otherwise set it to 1 */
                                        if(isset($_GET['page'])) {
                                            $currentPage = $_GET['page'];
                                        } else {
                                            $currentPage = 1;
                                        }
                                        /* Set how many orders should display per page */
                                        $ordersPerPage = 10;
                                        getPaginatedOrders($currentPage, $ordersPerPage);
                                        ?>
                                    </tbody>
                                </table>
                            </div> <!-- mytable -->
                        </div> <!-- table-responsive -->
                    </div> <!-- card-body -->

                    <!-- Card footer --- PAGINATION -->                  
                    <div class="card-footer pb-5 d-flex justify-content-end">
                    <nav aria-label="Page navigation">
                            <ul class="pagination">

                            </ul> <!-- pagination -->
                        </nav><!-- page navigation -->
                    </div> <!-- card-footer -->

                    <!-- Row og col-12 fyrir skilaboð sem koma í gegnum url -->
                    <div class="row">
                        <div class="col-12">
                            <?php
                            /* Check for msg in the URL and if so, display it in new row and col */
                            if(isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo '<div class="row">';
                                echo '<div class="col-12">';
                                echo "<div class='alert alert-success center'>$message</div>";
                                echo '</div>';
                                echo '</div>';
                                
                            }
                            ?>
                        </div> <!-- col-12 -->
                    </div> <!-- row -->
                </div> <!-- card -->
            </div> <!-- center -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->

<!--
    table: orders
    1	order_id Primary
	2	order_unique_id	
	3	user_id	int
	4	firstname
	5	lastname	
	6	email	
	7	address
	8	address2	
	9	postalcode	
	10	city	
	11	state
	12	country	
	13	created_at	
	14	final_price

    table: order_items
    1	order_items_id
	2	order_unique_id 	
	3	order_id
	4	product_id	
	5	quantity	
	6	price
	7	total_price

    table: order_process
    1	order_process_id
    2	order_unique_id	
	3	order_id Index	
	4	card_holder_name
	5	card_number
	6	card_expiry_month
	7	card_expiry_year
	8	cvv
	9	transaction_id	
	10	payment_status	
	11	created_at	
	12	final_price
                        -->