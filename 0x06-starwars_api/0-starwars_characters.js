#!/usr/bin/node

const axios = require('axios');
const process = require('process');

async function getMovieData(movieId) {
  try {
    const response = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    return response.data;
  } catch (error) {
    return null;
  }
}

async function getCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    return null;
  }
}

async function main() {
  if (process.argv.length !== 3) {
    console.log("Usage: ./script.js <movie_id>");
    process.exit(1);
  }

  const movieId = process.argv[2];
  const movieData = await getMovieData(movieId);

  if (!movieData) {
    console.log(`Movie with ID ${movieId} not found.`);
    return;
  }

  const characterUrls = movieData.characters;
  for (const characterUrl of characterUrls) {
    const characterName = await getCharacterName(characterUrl);
    if (characterName) {
      console.log(characterName);
    } else {
      console.log(`Could not retrieve character name from ${characterUrl}`);
    }
  }
}

main();

