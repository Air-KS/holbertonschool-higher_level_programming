// Get 'add_item' element and assign to 'addItemButton'
const addItemButton = document.getElementById('add_item');

// Get element with class 'my_list' and assign to 'myList'
const myList = document.querySelector('.my_list');

// Initialize a counter to keep track of the number of items added
let itemCount = 0;

// On button click, execute 'addItemToList'
addItemButton.addEventListener('click', addItemToList);

// Function to add a new item to the list
function addItemToList() {
  // Increment the item counter
  itemCount++;

  // Create a new <li> element
  const newItem = document.createElement('li');

  // Set text of new element to "Item" with its number
  newItem.textContent = `Item ${itemCount}`;

  // Add new <li> to 'myList'
  myList.appendChild(newItem);
}
