#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (_error, _response, body) => {
  if (body) {
    try {
      const filmsData = JSON.parse(body);
      for (let i = 0; i < filmsData.results.length; i++) {
        const film = filmsData.results[i];
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  }
});
