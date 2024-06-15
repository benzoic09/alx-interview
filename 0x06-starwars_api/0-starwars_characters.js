#!/usr/bin/node
const axios = require('axios');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// URL to fetch the specific movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch and print each character's name
const fetchCharacter = async (url) => {
  try {
    const response = await axios.get(url);
    console.log(response.data.name);
  } catch (error) {
    console.error('Error:', error.message);
  }
};

// Make the HTTP GET request to fetch movie details
axios.get(url)
  .then(response => {
    const characterUrls = response.data.characters;

    // Fetch and print each character's name in order
    characterUrls.forEach(url => fetchCharacter(url));
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
