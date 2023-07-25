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

function getPaginatedProducts($page, $perPage) {
    global $conn;
    // Finna út hvað margar rows skal skippa áður en náð er í tíu rows
    $offset = ($page - 1) * $perPage;
    /* Undirbý stmt, vel úr users         LIMIT startRow limit */
    $stmt = $conn->prepare("SELECT * FROM products LIMIT ?, ?");
    if(!$stmt) {
        echo "error in preparing the query: " . $conn->error;
    }
    /* Bind the parameters */
    $stmt->bind_param('ii', $offset, $perPage);
    /* Keyri statementið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
    }
    /* næ í niðurstöður */
    $result = $stmt->get_result();
    /* Athuga hvort niðurstöður hafi komið */
    if ($result->num_rows === 0) {
        echo "no rows returned";
    }
    /* Lúppa í gegnum result */
    while ($row = $result->fetch_assoc()) {
        $product_id = $row['product_id'];
        $image = $row['image'];
        $name = $row['name'];
        $description = $row['description'];
        $price = $row['price'];
        $category_id = $row['category_id'];

        echo "<tr>";
        echo "<td>$product_id</td>";
        echo "<td><img src='img/$image' alt='Product Image' class='' style='height: 75px; width: 75px; border: none;'></td>";
        echo "<td>$name</td>";
        echo "<td>$description</td>";
        echo "<td>$price</td>";
        echo "<td>$category_id</td>";
        echo "<td>
        <a class='btn btn-outline-secondary' href='products_action.php?source=products&product_id=" . $product_id . "&action=view'>View</a>
        <a class='btn btn-outline-danger' href='products_action.php?source=products&product_id=" . $product_id . "&action=delete'>Delete</a>
            </td>";
        echo "</tr>";
    }
}
/* ---- EKKI AÐ NOTA Á ÞESSARI SÍÐU ---- */
/*
function getCategoryName($category_id) {
    global $conn;
    $stmt = $conn->prepare("SELECT name FROM categories WHERE category_id = ?");
    if (!$stmt) {
        echo "Error in preparing the query: " . $conn->error;
        return;
    }
    $stmt->bind_param("i", $category_id);
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }
    $result = $stmt->get_result();
    if ($result->num_rows === 0) {
        echo "no rows found";
    }
    else {
        $row = $result->fetch_assoc();
        $category_name = $row['name'];
        $stmt->close();
        return $category_name;
    }
}
 */
/* Function sem telur hvað mörg rows eru í table database */
function countProducts() {
    global $conn;
    $stmt = $conn->prepare("SELECT count(*) FROM products");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    /* set töluna í breytu */
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
                    <!-- <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius" style="width: 95%;">List of your products</h4> -->
                    <h4 class="alert alert-success rounded-pill minnborderradius center" style="width: 95%;">List of your products</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col">Product ID</th>
                                            <th scope="col">Image</th>
                                            <th scope="col">Name</th>
                                            <th scope="col">Description</th>
                                            <th scope="col">Price</th>
                                            <th scope="col">Category ID</th>
                                            <th scope="col" class="action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>

                                        <?php
                                        /* Check if page is set in the url. Otherwise set the page to 1 */
                                        if(isset($_GET['page'])) {
                                            $currentPage = $_GET['page'];
                                        } else {
                                            $currentPage = 1;
                                        }
                                        $productsPerPage = 10;
                                        getPaginatedProducts($currentPage, $productsPerPage);
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
                                <?php 
                                /* Nota ceil til að rounda upp deilingu og finna út hvað margar síður eru */
                                $totalPages = ceil(countProducts() / $productsPerPage);
                                
                                /* Previous link */
                                if ($currentPage > 1) {
                                    /* set the link active if page number is more then 1 - Set the link to currentPage - 1 to the previous page */
                                    echo '<li class="page-item bg-dark"><a class="page-link" href="products.php?page=' . ($currentPage - 1) . '">Previous Page</a></li>';
                                } else {
                                    /* set the link as disabled if page number is 1 - the link hrefs to nothing since there is no previous page */
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>';
                                }
                                
                                /* Make the page numbers */
                                for ($i=1; $i <= $totalPages; $i++) {
                                    /* Þegar i er jafnt og currentPage þá er page-item ACTIVE */
                                    if ($currentPage == $i) {
                                        echo '<li class="page-item active"><a class="page-link" href="products.php?page=' . $i . '">' . $i . '</a></li>';
                                    }
                                    /* í öll önnur skipti sem i keyrir þá er page-item ekki active */
                                    else {
                                        echo '<li class="page-item"><a class="page-link" href="products.php?page=' . $i . '">' . $i . '</a></li>';
                                    }
                                }

                                /* Next link */
                                if ($currentPage < $totalPages) {
                                    echo '
                                    <li class="page-item">
                                    <a class="page-link" href="products.php?page=' . ($currentPage + 1) . '">Next Page</a>
                                    </li>
                                    ';
                                } else {
                                    echo '
                                    <li class="page-item disabled"><a class="page-link" href="#">Next Page</a></li>
                                    ';
                                }
                                ?>
                            </ul> <!-- pagination -->
                        </nav><!-- page navigation -->
                    </div> <!-- card-footer -->

                    <!-- Row og col-12 fyrir skilaboð sem koma í gegnum url -->
                    <div class="row">
                        <div class="col-12">
                            <?php 
                            if(isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo "<div class='alert alert-success center'>$message</div>";
                            }
                            ?>
                        </div> <!-- col-12 -->
                    </div> <!-- row -->
                </div> <!-- card -->
            </div> <!-- center -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->