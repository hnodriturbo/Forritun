<!-- Navbarið sem er efst á síðunni - Það expandar niður og er með leit -->
<nav class="navbar bg-dark fixed-top kirsty-regular-italic" data-bs-theme="dark">
  <div class="container-fluid">
    
    <a class="navbar-brand navbar-dark" href="#">
      Admin síða Crystal 3D Pictures
    </a>

    <!-- Þetta er takkinn með þremur strikum sem opnar navbar og lokar -->
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>

        
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <ul class="navbar-nav"> <!-- me-auto mb-2 mb-lg-0 -->

        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">
            Admin Overview
          </a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#">Vefverslun</a>
        </li>

        <li class="nav-item">
          <a class="nav-link" href="#">Útskráning</a>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Menu items
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="index.php">Overview</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="products.php">Products</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="orders.php">Orders</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="users.php">Users</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="categories.php">Categories</a></li>
            <li><hr class="dropdown-divider"></li>
            
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Leita
          </a>
          <ul class="dropdown-menu">
            <form role="search">
              <div class="row">
                <div class="col-lg-5 col-md-10">
                  <div class="row">
                    <div class="col-12">
                      <ul>
                        <input type="checkbox" id="products" name="products" value="Products">
                        <label for="products">Products</label>

                        <input type="checkbox" id="users" name="users" value="Users">
                        <label for="users">Users</label>

                        <input type="checkbox" id="orders" name="orders" value="Orders">
                        <label for="orders">Orders</label>

                        <input type="checkbox" id="everything" name="everything" value="Everything">
                        <label for="everything">Everything</label>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-5 col-md-10">
                  <div class="row">
                    <div class="col-12">

                      <input class="form-control" type="search" placeholder="Search" aria-label="Search">
                      <button class="btn btn-secondary" type="submit" style="width: 100%;">Search</button>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </ul>
        </li>

      </ul><!-- navbar-nav -->
    </div><!-- collapse navbar-collapse -->
        
  </div><!-- container-fluid -->

</nav><!-- navbar bg-dark fixed-top kirsty-regular-italic -->

   