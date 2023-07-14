

   <!--   Þessi takki togglar navbar upp og niður held ég -->
   
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" onclick="toggleSidebar()">
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Takki sem togglar offcanvas -->
    <button class="btn btn-primary position-absolute" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas" aria-controls="offcanvas">
        Button with data-bs-target
    </button>


    

<!--    
<nav class="navbar navbar-expand-lg navbar-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link 1</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link 2</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link 3</a>
      </li>
    </ul>
  </div>
</nav>
 -->
 
 <!-- Þetta er leið til að gera gegnsæjan bakgrunnsmynd -->   
<!-- style="background-image: linear-gradient(rgba(33, 37, 41, 0.9), rgba(33, 37, 41, 0.9)), url('img/backgroundsidebar.jpg');" -->




    <!-- ---------------- Offcanvas sem ég ætla geyma aðeins -->

    <!-- Takki sem togglar offcanvas -->
    <button class="btn btn-primary position-absolute" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas" aria-controls="offcanvas">
        Button with data-bs-target
    </button>



                    <!-- OFFCANVAS -->
<!-- -------------------------------------------------------------------- -->



<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasLabel">Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="index.php"> <!-- Added btn-lg class -->
        <i class="bi bi-person-circle" style="padding: 10px;"></i>
        <span>Overview</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="products.php">
        <i class="bi bi-card-list" style="padding: 10px;"></i>
        <span>Products</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="orders.php">
        <i class="bi bi-card-list" style="padding: 10px;"></i>
        <span>Orders</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="users.php">
        <i class="bi bi-person-circle" style="padding: 10px;"></i>
        <span>Users</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="categories.php">
        <i class="bi bi-box" style="padding: 10px;"></i>
        <span>Categories</span>
      </a>
    </li>

    <hr class="my-horizontal-line" style="width: 100%">

    <li class="nav-item">
      <a class="nav-link btn btn-outline-secondary rounded-pill" href="logout.php">
        <i class="bi bi-box-arrow-left" style="padding: 10px;"></i>
        <span>Log Out</span>
      </a>
    </li>
              

  </div>
</div>





<nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ">
        <div class="container-fluid">
          <div class="navbar-dark">
            <a class="navbar-brand" href="javascript:void(0)">Admin</a>
            
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end">
            <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link" href="javscript:void(0)" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="material-icons">person</i>
                  
                  <p class="d-lg-none d-md-block">
                    Some Actions
                  </p>
                </a>
                
              </li>
             
            </ul>
          </div>
        </div>
      </nav>
 <!-- 
   <div class="pos-f-t">
  <div class="collapse" id="navbarToggleExternalContent">
    <div class="bg-dark p-4">
      <h4 class="text-white">Collapsed content</h4>
      <span class="text-muted">Toggleable via the navbar brand.</span>
    </div>
  </div>
  <nav class="navbar navbar-dark bg-dark">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  </nav>
</div>
  
 -->








  













