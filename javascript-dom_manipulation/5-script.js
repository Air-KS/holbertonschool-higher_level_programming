// Retrieve the button element with ID 'update_header'
const updateHeaderButton = document.getElementById('update_header');

// On click, update header text
updateHeaderButton.addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
