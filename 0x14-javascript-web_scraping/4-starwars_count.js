#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <API_URL>');
  return ;
}
const url = process.argv[2];
let count = 0;
request(url, (_error, _response, body) => {
  if (body) {
    try {
      const filmsData = JSON.parse(body);
      for (let i = 0; i < filmsData.results.length; i++) {
        const film = filmsData.results[i];
        if (film.characters.some(characterUrl => characterUrl.endsWith(`people/${characterId}/`))) {
          count++;
        }
      }
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  }
});
