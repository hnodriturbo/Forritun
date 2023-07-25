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
        font-family: 'customFont';
        src: url('font/Eastwood/Eastwood.woff2') format('woff2'),
            url('font/Eastwood/Eastwood.woff') format('woff'),
            url('font/Eastwood/Eastwood.ttf') format('truetype');
      }

      @font-face {
      font-family: 'kirstyRegular';
      src: url('font/kirsty/kirsty_rg.otf') format('opentype');
      }

      @font-face {
      font-family: 'kirstyRegularItalic';
      src: url('font/kirsty/kirsty_rg_it.otf') format('opentype');
      }

      @font-face {
      font-family: 'kirstyBold';
      src: url('font/kirsty/kirsty_bd.otf') format('opentype');
      }

      @font-face {
      font-family: 'kirstyBoldItalic';
      src: url('font/kirsty/kirsty_bd_it.otf') format('opentype');
      }

      .custom-text {
      font-family: 'customFont', sans-serif;
      }

      .kirsty-regular {
      font-family: 'kirstyRegular', sans-serif;
      }

      .kirsty-regular-italic {
      font-family: 'kirstyRegularItalic', sans-serif;
      }

      .kirsty-bold {
      font-family: 'kirstyBold', sans-serif;
      }

      .kirsty-bold-italic {
      font-family: 'kirstyBoldItalic', sans-serif;
      }

      </style>
    <!-- Titill síðunnar -->
    <title>Admin - Crystal 3D Pictures</title>
  
</head>


<body> 
  <div class="container-fluid mittmargin"><!-- container utan um allt --> <!-- div lokast ekki -->
    <div class="row"><!-- rowið utan um allt --> <!-- div lokast ekki -->


      <div class="col-2 col-lg-2 vh-100 d-none d-lg-flex align-items-center justify-content-center position-fixed">
        <div class="container-fluid backgroundsidebar">
          <div class="sidebar sidebar-colors mb-lg-0 d-none d-lg-block kirsty-bold-italic" ><!-- -->
            
            <nav class="navbar navbar-expand-lg">

              <ul class="nav flex-column w-75 mx-auto align-items-center">

                <li class="nav-item">
                <div class="nav-link"><span>Admin</span></div>
                </li>

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="index.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Overview</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="orders.php">
                    <i class="bi bi-card-list" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Orders</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="products.php">
                    <i class="bi bi-grid-3x3-gap-fill" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Products</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="categories.php">
                    <i class="bi bi-box" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Categories</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="users.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Users</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="logs.php">
                    <i class="bi bi-globe2" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Logs</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="admins.php">
                    <i class="bi bi-person-circle" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Admins</span>
                  </a>
                </li>

                <hr class="my-horizontal-line" style="width: 100%">

                <li class="nav-item w-100">
                  <a class="nav-link btn btn-outline-secondary rounded-pill d-flex align-items-center" href="logout.php">
                    <i class="bi bi-box-arrow-left" style="padding: 0; margin-right: 20px;"></i>
                    <span class="ml-2">Log Out</span>
                  </a>
                </li>
              </ul><!-- nav flex-column w-75 mx-auto align-items-center -->
            </nav><!-- navbar navbar-expand-lg -->
            
          </div><!-- sidebar sidebar-colors mb-lg-0 d-none d-lg-block kirsty-bold-italic -->
        </div><!-- container-fluid backgroundsidebar -->
      </div> <!-- col-2 col-lg-2 vh-100 d-none d-lg-flex align-items-center justify-content-center position-fixed -->


