#!/usr/bin/node
const request = require('request');

const getCharactersFromMovies = (movieId) => {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/';
  request(`${baseUrl}films`, function (error, reponse, body) {
    if (error) return;
    const films = JSON.parse(body).results;
    if (movieId < 1 || movieId > films.lenght) return;
    const film = films[movieId - 1];
    const characters = film.characters;

    characters.map(url => request(url, function (err, resp, body) {
      if (err) return;
      const character = JSON.parse(body);
      console.log(character.name);
    }));
  });
};

const args = process.argv.slice(2);
if (args.length !== 1) {
  process.exit(1);
} else {
  const movieId = parseInt(args[0], 10);
  if (isNaN(movieId)) {
    process.exit(1);
  } else {
    getCharactersFromMovies(movieId);
  }
}
