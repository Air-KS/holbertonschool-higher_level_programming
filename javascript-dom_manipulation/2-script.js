// Select the header element using document.querySelector
const header = document.querySelector('header');
// Get the element with id 'red_header'
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', () => {
  // Add the class 'Red' to header element
  header.classList.add('red');
});
