#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (_error, response, body) => {
  if (response && response.statusCode >= 200 && response.statusCode < 300) {
    try {
      const filmsData = JSON.parse(body);
      const filmsWithWedge = filmsData.results.filter((film) => {
        return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
      });
      if (filmsWithWedge.length > 0) {
        console.log(filmsWithWedge.length);
      } else {
        console.log(0);
      }
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  }
});
