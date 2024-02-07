#!/usr/bin/node
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

const fetchTitle = async () => {
  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`Failed to fetch data. Status: ${response.status}`);
    }
    const data = await response.json();
    const titles = data.results;
    const list = $('UL#list_movies');
    titles.forEach(movie => {
      const item = '<li>' + movie.title + '</li>';
      list.append(item);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
};
fetchTitle();
