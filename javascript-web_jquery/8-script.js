/* global $ */
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

  fetch(url)
  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    for (let movie of movies) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    }
  })
  .catch(error => console.error('Error witch fetch :', error));
});
