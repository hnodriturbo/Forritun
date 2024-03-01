////////////////////* ########## Hreiðar Pétursson ########## *////////////////////
////////////////////*  ######## Javascript Áfanginn ########  *////////////////////
////////////////////*   ######### Skilaverkefni 5 #########   *////////////////////
////////////////////*    ########  Febrúar 2024   ########    *////////////////////
////////////////////*     #######   SPA  Events   #######     *////////////////////


/* 
// Fetch events function
function fetchEvents() {
    fetch('vidburdir.json')
        .then(response => response.json())
        .then(events => {
            displayEvents(events);
        })
        .catch(error => {
            console.error('Error fetching the events: ', error);
        });
} */


// Async to fetch events, sort them by price, and display them
async function fetchEvents() {
    try {
        const response = await fetch('vidburdir.json'); // Adjust the path if necessary
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const events = await response.json(); // Parse the JSON data

        // Sort events by price in ascending order
        events.sort((a, b) => a.price - b.price);

        displayEvents(events); // Display the sorted events

        initSlider(events); // Initialize the slider

    } catch (error) {
        console.error('Error fetching the events:', error);
    }
}




function displayEvents(events) {
    const container = document.getElementById('events-container');
    container.innerHTML = ''; // Clear existing content

    events.forEach(event => {
        const eventCard = document.createElement('div');
        eventCard.className = 'col-sm-12 col-md-6 col-lg-4 mb-4'; // For responsive behaviour
        

        const cardHTML = `
            <div class="my-card h-100 d-flex flex-column">
                
                <img src="${event.image}" class="my-image-top" alt="${event.name}">

                <div class="my-card-body flex-grow-1">
                    <h5 class="my-card-title">${event.name}</h5>
                    <p class="my-card-text short-description">${event.description}</p>
                </div>

                <div class="d-flex my-card-footer mt-auto align-items-center justify-content-center flex-column">
                    <div class="row">
                        <p class="my-card-price">Price: ${event.price} kr.-</p>
                    </div>
                    <div class="row">
                        <p class="my-card-date">${dayjs(event.date).format('D MMMM YYYY')}</p>
                    </div> 
                </div>

            </div>
        `;

        // Set the HTML as innerHTML in the eventCard
        eventCard.innerHTML = cardHTML;
        
        // Append the eventCard to the container
        container.appendChild(eventCard);

        
        eventCard.addEventListener('click', function() {
            // Corrected modal content, ensuring it's using modal-specific classes or styles if needed
            const modalCardHTML = `
                <div class="modal-card">
                    <img src="${event.image}" alt="${event.name}" class="my-image-top">
                    <div class="modal-card-body">
                        <h5 class="modal-card-title">${event.name}</h5>
                        <p class="modal-card-text">${event.description}</p>
                        <p class="modal-card-price">Price: ${event.price} kr.-</p>
                        <p class="modal-card-date">${dayjs(event.date).format('D MMMM YYYY')}</p>
                    </div>
                </div>
                <span class="close-button">&times;</span>`; // Ensuring the close button is included
        
            openModal(modalCardHTML); // Pass the constructed HTML to openModal
        });
        


    }); // end of events.forEach(event =>......)


}       




function openModal(contentHTML) {

    const modal = document.getElementById('eventModal');
    const modalContent = document.getElementById('modalContent');

    modalContent.innerHTML = contentHTML; // Use provided HTML content
    modal.style.display = 'flex'; // Display the modal
    modal.style.opacity = 1; // Ensure modal visibility


    // Add a event listener for the close button so the modals closes when close btn is clicked
    document.querySelector('.close-button').addEventListener('click', closeModal);

    // Prevent event bubbling (the modal closing when clicking inside of the modal)
    modalContent.addEventListener('click', function(event) {
        event.stopPropagation();
    });

}


// Function to close the modal, set display to none
function closeModal() {
    const modal = document.getElementById('eventModal');
    modal.style.display = 'none';
}

// Event listener to close the modal when clicking anywhere outside the modal
document.addEventListener('click', function(event) {
    const modal = document.getElementById('eventModal');
    if (event.target === modal) {
        closeModal();
    }
});

/* 
function openModal() {
    const modal = document.getElementById('eventModal');
    modal.style.display = 'flex';
    modal.style.opacity = 1; // Fade in animation structure
}

// Function for resetting the modal's state before opening (making sure the opacity is at 0.1)
function resetModal() {
    const modal = document.getElementById('eventModal');
    modal.style.display = 'none';
    modal.style.opacity = 0.1; // Reset the opacity
}

function closeModal() {
    const modal = document.getElementById('eventModal');
    modal.style.display = 'none';
}

document.querySelector('.close-button').addEventListener('click', closeModal);

 */








/* ----- ----- Slider function ----- ----- */

function initSlider(events) {
    const slider = document.getElementById('price-slider');
    const minPrice = Math.min(...events.map(event => event.price));
    const maxPrice = Math.max(...events.map(event => event.price));

    noUiSlider.create(slider, {
        start: [minPrice, maxPrice],
        connect: true,
        range: {
            'min': minPrice,
            'max': maxPrice
        },
        step: 1
    });

    slider.noUiSlider.on('update', function(values, handle) {
        const [minValue, maxValue] = values.map(value => parseFloat(value));
        const filteredEvents = events.filter(event => event.price >= minValue && event.price <= maxValue);
        displayEvents(filteredEvents);
    });
}



/* ATHUGA SEARCH ER EKKI AÐ VIRKA Í AUGNABLIKINU !!!!!! GERA MODAL Í STAÐINN Á MEÐAN ÉG FINN ÚTÚR SEARCH */
/* Search field Event listener for the input of keystrokes */

document.getElementById('event-search').addEventListener('input', function() {
    const searchQuery = this.value.toLowerCase();
    const filteredEventsBySearch = allEvents.filter(event => event.name.toLowerCase().includes(searchQuery));
    displayEvents(filteredEventsBySearch);
});








/* ---------- Extras - Toggle between classes for box shadow animation effect ---------- */

// My toggling between functions effect (usually between different box shadows for glowing effect)
function startToggleEffect() {
    // When page is fully loaded, fetch the events and display them
    const elements = document.querySelectorAll('.my-box-shadow-animation');
    // If there are any elements with this class
    if (elements.length > 0) {
        // Set the interval method to 1000ms or 1 second between classes
        setInterval(() => {
            elements.forEach(element => {
                element.classList.toggle('my-box-shadow-animation-toggle');
            });
        }, 1000);
    }
}

function initializeBoxShadowToggle() {
    // Select all elements with the .my-btn-box-shadow class
    const btnElements = document.querySelectorAll('.my-btn-box-shadow');
    // Function to add the toggle class
    const addToggleEffect = (element) => {
        element.classList.add('my-box-shadow-animation-toggle');
    };
    // Function to remove the toggle class
    const removeToggleEffect = (element) => {
        element.classList.remove('my-box-shadow-animation-toggle');
    };
    // Attach event listeners to each element
    btnElements.forEach(element => {
        element.addEventListener('mouseenter', () => addToggleEffect(element));
        element.addEventListener('mouseleave', () => removeToggleEffect(element));
    });
}






/* Finally, wait for the Document Object Model to complete it's */
         /* loading and then execute these functions */

document.addEventListener('DOMContentLoaded', () => {

    // When page is fully loaded, fetch the events and display them
    fetchEvents()

    // Start the toggle effect if there are any elements with the selected class
    startToggleEffect();

    // Box shadow effect on menu buttons on mouse hover
    initializeBoxShadowToggle()


});























/* -------------- Storage ----------- */



/* 

// Call fetchEvents when the document is loaded
document.addEventListener('DOMContentLoaded', fetchEvents);





// Call fetchEvents when the document is loaded
document.addEventListener('DOMContentLoaded', fetchEvents);




 */

/* 
const cardHTML = `
<div class="my-card h-100">
    
    <img src="${event.image}" class="my-image-top" alt="${event.name}">

    <div class="my-card-body">
    
        <h5 class="my-card-title">${event.name}</h5>
        <p class="my-card-text">${event.description}</p>
        <p class="my-card-text">${event.price} kr.-</p>
        <p class="my-card-text">${dayjs(event.date).format('D MMMM YYYY')}</p>
    </div>



</div>


`; */

/* 
        // Add click event listener to each card for opening the modal
        eventCard.addEventListener('click', function() {
            const modalBody = document.getElementById('modal-content');

            modalBody.innerHTML = cardHTML; // Usage of the same card as the modal body

            // If i add more details to this modal (since it is for more information i have yet to create)
            const moreDetails = document.createElement('p');
            moreDetails.textContent = event.extraDescription;
            modalBody.appendChild(moreDetails);


            openModal(); // Open Modal function on click of the event */