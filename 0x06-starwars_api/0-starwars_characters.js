#!/usr/bin/node
const axios = require('axios');

// Function to get characters for a given movie ID
const getCharactersFromMovie = async (movieId) => {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/';

  try {
    // Fetch the list of films
    const filmsResponse = await axios.get(`${baseUrl}films/`);

    const films = filmsResponse.data.results;

    // Validate Movie ID
    if (movieId < 1 || movieId > films.length) {
      console.log(`Movie ID ${movieId} is out of range. Please provide a valid ID.`);
      return;
    }

    const film = films[movieId - 1];

    // Print the film title for context
    console.log(`Characters from: ${film.title}`);

    // Fetch and print each character's name
    const characterUrls = film.characters;

    for (const url of characterUrls) {
      const characterResponse = await axios.get(url);
      const character = characterResponse.data;
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
};

// Command-line argument handling
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: node star_wars_characters.js <Movie ID>');
} else {
  const movieId = parseInt(args[0], 10);
  if (isNaN(movieId)) {
    console.log('Please provide a valid integer for the Movie ID.');
  } else {
    getCharactersFromMovie(movieId);
  }
}
