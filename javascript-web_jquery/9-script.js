/* global $ */
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
  .then(response => response.json())
  .then(data => {
    $('#hello').text(data.hello);
  })
  .catch(error => console.error('Error with fetch :', error));
});
