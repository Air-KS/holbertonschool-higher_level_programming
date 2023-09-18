/* global $ */
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
  .then(response => response.json())
  .then(data => {
    $('#character').text(data.name);
  })
  .catch(error => console.error('error with fetch :', error));
});
