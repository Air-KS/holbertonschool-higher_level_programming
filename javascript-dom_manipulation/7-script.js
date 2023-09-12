// Retrieve the DOM element with the ID 'list_movies'
const movieListElement = document.getElementById('list_movies');

// Check if the element exists before proceeding
if (movieListElement) {  // Vérifier si l'élément existe
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

    // Fetch movie data from the API
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => displayMovies(data.results))
        .catch(error => {
            console.error(error);
        });
}

// Function to display the list of movies on the webpage
function displayMovies(movies) {
    movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        movieListElement.appendChild(listItem);
    });
}
