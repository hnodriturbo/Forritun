/* ########## Hreiðar Pétursson ########## */
/*  ######## Javascript Áfanginn ########  */
/*   ######### Skilaverkefni 5 #########   */
/*    ########  Febrúar 2024   ########    */
/*     #######   SPA  Events   #######     */


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
        initSlider(events); // Initialize the slider, if applicable
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

        eventCard.innerHTML = cardHTML;
        container.appendChild(eventCard);
    });
}



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



document.getElementById('event-search').addEventListener('input', function() {
    const searchQuery = this.value.toLowerCase();
    const filteredEventsBySearch = allEvents.filter(event => event.name.toLowerCase().includes(searchQuery));
    displayEvents(filteredEventsBySearch);
});















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



document.addEventListener('DOMContentLoaded', () => {
    // Box shadow effect on menu buttons on mouse hover
    initializeBoxShadowToggle()
    // When page is fully loaded, fetch the events and display them
    fetchEvents()

    // Start the toggle effect if there are any elements with the selected class
    startToggleEffect();


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