// Wait for the entire DOM to load before executing the script
document.addEventListener("DOMContentLoaded", function() {

  // Get references to the list and the action div elements
  const myList = document.querySelector('.my_list');
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');

  // Add event listener to the "Add item" div to add a new list item
  if (addItem) {
      addItem.addEventListener('click', function() {
          const li = document.createElement('li');
          li.textContent = 'Item';
          myList.appendChild(li);
      });
  }

  // Add event listener to the "Remove item" div to remove the last list item
  if (removeItem) {
      removeItem.addEventListener('click', function() {
          const lastItem = myList.lastElementChild;
          if (lastItem) {
              myList.removeChild(lastItem);
          }
      });
  }

  // Add event listener to the "Clear list" div to clear all list items
  if (clearList) {
      clearList.addEventListener('click', function() {
          myList.innerHTML = '';
      });
  }

});
