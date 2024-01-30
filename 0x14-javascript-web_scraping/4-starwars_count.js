#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
request(url, (_error, response, body) => {
  if (response && response.statusCode >= 200 && response.statusCode < 300) {
    try {
      const filmsData = JSON.parse(body);
      const filmsWithWedge = filmsData.results.filter((film) => {
        return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
      });
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  } else {
    console.error('Film Not Found!');
  }
});
