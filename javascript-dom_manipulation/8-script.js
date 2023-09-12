/**
 * Fetches the translation of "hello" from an API and displays it in an element.
 */
const fetchHelloTranslation = () => {
  // Select the HTML element with the id "hello"
  const helloElement = document.getElementById('hello');
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Retrieve the translation from the API
  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response not OK');
      }
      return response.json();
    })
    .then(data => {
      // Check the structure of the data
      if (data && data.hello) {
        helloElement.textContent = data.hello;
      } else {
        throw new Error('Unexpected data structure');
      }
    })
    .catch(error => {
      console.error('Error during the request:', error);
    });
}

// Call the function when the document is fully loaded
document.addEventListener('DOMContentLoaded', fetchHelloTranslation);
