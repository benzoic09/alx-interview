#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

// URL to fetch the specific movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the HTTP GET request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
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

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  };

  // Fetch and print each character's name in order
  characterUrls.forEach(fetchCharacter);
});
