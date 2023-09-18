/* global $ */

$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(url, function(data) {
    $('#update_header').text(data.name);
  });
});

/*
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
  .then(response => response.json())
  .then(data => {
    $('#update_header').text(data_name);
  })
  .catch(error => console.error('error with fetch :', error));
});
*/
