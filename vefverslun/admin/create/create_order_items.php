

<?php
echo '

<div class="card-body card-body-add-order">
       <div class="alert alert-success borderradius">
              <div class="row m-1 text-black">
                     <div class="col-8 align-items-start justify-content-start d-flex">
                     <h2>Step 3 - Add Items To Order</h2>
                     </div>
                     <div class="col-4 align-items-end justify-content-end d-flex">
                     <h2>Create Order</h2>
                     </div>  
              </div>
       </div>
       <hr class="my-horizontal-line"></hr>    <!-- Línan -->
       <hr class="my-horizontal-line-black"></hr>    <!-- Línan -->

       <form id="create-order-step-3" class="needs-validation" novalidate>

       <!-- FIRSTNAME - LASTNAME - EMAIL -->
       <div class="row p-1 align-items-center justify-content-center d-flex">
              <div class="col-lg-8 col-12">
                     <div class="row">
                            <div class="col-4 d-flex align-items-center justify-content-center">
                                   <label for="validationDefault01" class="nowrap whitetext font-size-22px">Firstname:</label>
                            </div>
                            <div class="col-8">
                                   <input class="form-control bg-dark-subtle" 
                                   type="text" 
                                   name="firstname" 
                                   placeholder="Required field" 
                                   id="validationDefault01" 
                                   required>
                                   <div class="invalid-feedback">Name is required !</div>
                            </div>
                     </div>
              </div>
       </div> <!-- row p-1 align-items-center -->

       <br>

       <div class="row p-1 align-items-center justify-content-center d-flex">
              <div class="col-lg-8 col-12">
                     <div class="row">
                            <div class="col-4 d-flex align-items-center justify-content-center">
                                   <label class="nowrap whitetext font-size-22px">Lastname:</label>
                            </div>
                            <div class="col-8">
                                   <input class="form-control bg-dark-subtle" 
                                   type="text" 
                                   name="lastname" 
                                   placeholder="Required field"
                                   required>
                                   <div class="invalid-feedback">Lastname is required !</div>
                            </div>
                     </div>
              </div>
       </div> <!-- row p-1 align-items-center -->

       <br>


       <div class="row p-1 align-items-center justify-content-center d-flex">
              <div class="col-lg-8 col-12">
                     <div class="row">
                            <div class="col-4 d-flex align-items-center justify-content-center">
                                   <label class="nowrap whitetext font-size-22px">E-mail:</label>
                            </div>
                            <div class="col-8">
                                   <input class="form-control bg-dark-subtle" 
                                   type="text" 
                                   name="email" 
                                   placeholder="Required field"
                                   pattern="[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}$"
                                   required>
                                   <div class="invalid-feedback">Please enter a valid email address !</div>
                            </div>
                     </div>
              </div>
       </div> <!-- row p-1 align-items-center -->


       <hr class="my-horizontal-line-black"></hr>    <!-- Línan -->
       <hr class="my-horizontal-line"></hr>    <!-- Línan -->


';


?>