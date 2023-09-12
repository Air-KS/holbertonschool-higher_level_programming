// Select the header element using document.querySelector
const header = document.querySelector('header');
// Get the element with id 'toggle_header'
const toggleHeader = document.getElementById('toggle_header');

// Add a listener to 'toggleHeader' element
toggleHeader.addEventListener('click', function () {

  // Click to switch header between red and green.
  header.classList.toggle('red');
  header.classList.toggle('green');
});
