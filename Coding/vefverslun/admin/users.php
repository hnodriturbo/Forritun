<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

ob_start();
session_start();

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

function getPaginatedUsers($page, $perPage) {
    global $conn;

    // Finna út hvað margar rows skal skippa áður en náð er í tíu rows
    $offset = ($page - 1) * $perPage;
    /* Undirbý stmt, vel úr users         LIMIT startRow limit */
    $stmt = $conn->prepare("SELECT * FROM users LIMIT ?, ?");
    if (!$stmt) {
        echo "Error in preparing the query: " . $conn->error;
        return;
    }
    /* Bind the parameters */
    $stmt->bind_param('ii', $offset, $perPage);

    /* Keyri statementið */
    if(!$stmt->execute()) {
        echo "error in executing the query: " . $stmt->error;
        return;
    }

    /* næ í niðurstöður */
    $result = $stmt->get_result();

    /* Athuga hvort niðurstöður hafi komið */
    if ($result->num_rows === 0) {
        echo "no rows found";
    }


    /* Keyri í gegnum result með row = $result->fetch_assoc() */
    while ($row = $result->fetch_assoc()) {
        /* set hvern column úr row í breytur */
        $user_id = $row['user_id'];
        $user_uid = $row['user_uid'];
        $firstname = $row['firstname'];
        $lastname = $row['lastname'];
        $email = $row['email'];
        $username = $row['username'];
        $city = $row['city'];
        $country = $row['country'];
        $other = $row['other'];

        echo "<tr>";
        echo "<td>$user_id</td>";
        echo "<td>$firstname</td>";
        echo "<td>$lastname</td>";
        echo "<td>$email</td>";
        echo "<td>$username</td>";
        echo "<td>$city</td>";
        echo "<td>$country</td>";
        echo "<td>$other</td>";
        echo "<td><a class='btn btn-outline-secondary' href='useraction.php?action=view&source=users&user_uid=" . $user_uid . "'>View</a>
                  <a class='btn btn-outline-danger' href='useraction.php?action=delete&source=users&user_uid=" . $user_uid . "'>Delete</a>
        </td>";
        echo "</tr>";
    }
}

//Function sem telur total rows úr users
function countUsers() {
    global $conn;
    $stmt = $conn->prepare("SELECT count(*) FROM users");
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_array();
    $count = $row[0];
    return $count;
}
?>

<!-- Þessi col-lg-10 col-12 er utan um allt content síðunnar -->
<div class="col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset" style="font-size: 13px;">
    <!-- Container fyrir skipulag contents -->
    <div class="container-fluid">
        <!-- Row og col sem geymir Users table -->
        <div class="row">
            <div class="align-items-center justify-content-center center h-100 w-100 mx-auto">
                <!-- Cardið fyrir Users table -->
                <div class="card card-lg-width col-lg-10 col-12 mx-auto justify-content-center align-content-center" style="margin-top: 100px;">
                    <div class="card-header">
                    <h4 class="btn btn-dark btn-outline-secondary rounded-pill minnborderradius" style="width: 95%;">Users List</h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive border" style="overflow-x: auto;">
                            <div class="mytable">
                                <table class="table nowrap table-striped-columns table-dark table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col" class="first-column">User id</th>
                                            <th scope="col" class="name-column">Firstname</th>
                                            <th scope="col" class="name-column">Lastname</th>
                                            <th scope="col" class="email-column">E-mail</th>
                                            <th scope="col" class="name-column">Username</th>
                                            <th scope="col" class="name-column">City</th>
                                            <th scope="col" class="name-column">Country</th>
                                            <th scope="col" class="other-column">Other</th>
                                            <th scope="col" class="action-column">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                     <!-- Ef síða er skráð þá setja hana - annars set page to 1 -->
                                        <?php
                                        if(isset($_GET['page'])) {
                                            $currentPage = $_GET['page'];
                                        } else {
                                            $currentPage = 1;
                                        }
                                        // Ef síða er skráð þá setja hana - annars set page to 1
                                        $currentPage = isset($_GET['page']) ? $_GET['page'] : 1;
                                        $usersPerPage = 10;
                                        getPaginatedUsers($currentPage, $usersPerPage);
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
                                /* Nota ceil til að rounda deilingunni og finna út hvað margar síður eru */
                                /* (totalNotendur / hvadMargirPerSíðu) */
                                $totalPages = ceil(countUsers() / $usersPerPage);

                                /* Display "previous" link */
                                if ($currentPage > 1) {
                                    /* Ef síða er meira en 1 þá er linkurinn active */
                                    echo '<li class="page-item bg-dark"><a class="page-link" href="users.php?page=' . ($currentPage - 1) . '">Previous Page</a></li>';
                                } 
                                else {
                                    /* Ef síðan er númer 1 er previous takkinn disabled */
                                    echo '<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>';
                                }

                                /* Sýna síðunúmerin sjálf */
                                for ($i=1; $i <= $totalPages; $i++) {
                                    if ($currentPage == $i) {
                                        echo '<li class="page-item active"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';
                                        $active = ' active';
                                    } else {
                                        echo '<li class="page-item"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';
                                        $active = '';
                                    }
                                    /* echo '<li class="page-item' . ($active) . '"><a class="page-link" href="users.php?page=' . $i . '">' . $i . '</a></li>';  */
                                }

                                /* Display "next" link */
                                if ($currentPage < $totalPages) {
                                    echo '
                                    <li class="page-item">
                                    <a class="page-link" href="users.php?page=' . ($currentPage + 1) . '">Next Page</a>
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
                            if (isset($_GET['message'])) {
                                $message = $_GET['message'];
                                echo "<div class='alert alert-success center'>$message</div>";
                            }
                            ?>
                        </div> <!-- col-12 -->
                    </div> <!-- row -->
                </div> <!-- card -->
            </div> <!-- d-flex align-items-center justify-content-center h-100 col-lg-10 col-12 mx-auto -->
        </div> <!-- row -->
    </div> <!-- container-fluid -->
</div><!-- col-lg-10 col-12 d-lg-flex offset-lg-2 kirsty-regular-italic offset -->
