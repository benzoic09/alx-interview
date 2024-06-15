#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// URL to fetch the specific movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the HTTP GET request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data from API. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs
  const characterUrls = movieData.characters;

  // Function to fetch and print each character's name
  const fetchCharacter = (url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character data from API. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  };

  // Fetch and print each character's name in order
  characterUrls.forEach(fetchCharacter);
});
