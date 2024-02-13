/* ########## Hreiðar Pétursson ########## */
/*  ######## Javascript Áfanginn ########  */
/*   ######### Skilaverkefni 4 #########   */
/*    ######### Product List ##########    */
/*     #######   Febrúar 2024   ######     */


/* <!-- By the way - I use alot of comments in my codings --> */
/* <!-- And I always use the English language. --> */

/* I specificly designed this so the enter button doesnt work to insert products. */
/* addProduct() is only called on the button press (being designed for phones) */

/* Normally i would make the enter button work and use preventDefault() so the javascript */
/* manages the insertion of a product. I just don't use <form> in my HTML */

/* Reason for I make the error message is because if product is entered only with name and not */
/* a price, then the total would display as NaN. Price must be at least 0 if no price is to be inserted */


document.addEventListener('DOMContentLoaded', () => {

    // First get the elements by their ID
    const productNameInput = document.getElementById('productName');
    const productPriceInput = document.getElementById('productPrice');
    
    // Get the button element
    const addProductButton = document.getElementById('addProductButton');

    // Get the product element
    const productList = document.getElementById('productList');

    // Get the total price element
    const totalPriceDisplay = document.getElementById('totalPrice');


    /* Put the products into an array */
    let products = JSON.parse(localStorage.getItem('products')) || [];


    // Put five products only if the products length is 0 and first page load
    if (products.length === 0) {
        products = [
            { name: "Gatorade blár", price: 350 },
            { name: "Appelsín dós", price: 99 },
            { name: "Nocco Sunny Soda", price: 450 },
            { name: "Mjólk", price: 171 },
            { name: "Oreo kex", price: 290 }
        ];
        localStorage.setItem('products', JSON.stringify(products))
    }




    function formatISK(total) {
        const formatter = new Intl.NumberFormat('is-IS');
        const formattedAmount = formatter.format(total);
        return formattedAmount;
    }

    function calculateTotalPrice() {
        let total = 0;
        products.forEach(product => {
            total += parseFloat(product.price);
        });
        formattedTotal = formatISK(total);
        return formattedTotal;
    }

    // Function to display products - very simplified html
    // Need to add classes and make them for better look - this is raw
    function displayProducts() {
        // Make a empty variable for to later append the html
        productList.innerHTML = '';

        // Set total variable
        const total = calculateTotalPrice();

        if (products.length > 0) {
            // Use forEach loop to iterate through products and display them
            products.forEach((product, index) => {
                
                const productItem = document.createElement('li');
                productItem.classList.add('productItem');


                // Now create the columns for name, price and delete button
                
                // Create name column and add class to it and textContent
                const nameCol = document.createElement('div');
                nameCol.classList.add('productNameCol');
                nameCol.textContent = product.name;


                // Create price column and add class to it and textContent
                const priceCol = document.createElement('div');
                priceCol.classList.add('productPriceCol');
                const formattedProductPrice = formatISK(product.price);
                priceCol.textContent = `${formattedProductPrice} kr.-`; /* product.price */
    

                const deleteCol = document.createElement('div');
                deleteCol.classList.add('deleteButtonCol');

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.classList.add('deleteButton')

                /* Two ways available that i know for this... */
                deleteButton.onclick = function() { deleteProduct(index); }
                /* deleteButton.onclick = () => deleteProduct(index); */

                deleteCol.appendChild(deleteButton);

                // Append columns to the product item
                productItem.appendChild(nameCol);
                productItem.appendChild(priceCol);
                productItem.appendChild(deleteCol);

                productList.appendChild(productItem);

                /* total += parseFloat(product.price); */

            });

            


        } 
        
        else {
            const productElement = document.createElement('li');
            productElement.classList.add('productItem');
            productElement.textContent = `Found no products in local storage`;
            productList.appendChild(productElement);
        }
      
        // Write the total price calculated by the specific function
        totalPriceDisplay.textContent = `Total Price: ${total} kr.-`;

        /* totalPriceDisplay.textContent = total; */
    };   



    // Function for adding a product to localStorage
    function addProduct() {

        console.log('addProduct function called') // Debug statement

        // Get the productNameInput and productPriceInput values and trim them
        const productName = productNameInput.value.trim();
        const productPrice = productPriceInput.value.trim();

        // Debug statement.. this prints the values
        console.log(productName, productPrice);

        // Check if name is empty or price is empty
        if (productName === '' || productPrice === '') {
            document.getElementById('errorMessage').textContent = 'Please enter both product name and price !';
            document.getElementById('errorMessage').style.display = 'flex';
        }
        else {

            const productPriceNumber = parseFloat(productPrice);

            products.push({ name: productName, price: productPriceNumber });

            localStorage.setItem('products', JSON.stringify(products));

            displayProducts();

            productNameInput.value = '';
            productPriceInput.value = '';

            document.getElementById('errorMessage').style.display = 'none';

        }






    };


    // Function for deleting a product
    function deleteProduct(index) {
        products.splice(index, 1);
        localStorage.setItem('products', JSON.stringify(products));
        displayProducts();
    };



    // Add the event listener
    addProductButton.onclick = function() {
        addProduct();
    };
    /* addProductButton.addEventListener('click', addProduct(productNameInput, productPriceInput)); */
    

    // Display the products when the page loads
    displayProducts();




});







