// Get 'character' element and assign to 'characterElement'
const characterElement = document.getElementById('character');

// Define the API endpoint URL for fetching the character data
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

/*
  Fetch data from the API,
  convert the response to JSON,
  display the name, and handle any errors
*/
fetch(apiUrl)
  .then(verifyResponse)
  .then(response => response.json())
  .then(displayCharacterName)
  .catch(handleError);

// Check if the API response is successful
function verifyResponse(response) {
  if (!response.ok) {
    throw new Error(`Erreur HTTP: ${response.status}`);
  }
  // Return the valid response for further processing
  return response;
}

// Display the character name in the 'characterElement'
function displayCharacterName(data) {
  const { name } = data;  // Destructure to get 'name' from the data
  characterElement.textContent = name;
}

// Handle and log any errors
function handleError(error) {
  console.error(error);
}
