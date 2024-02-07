#!/usr/bin/node
const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

const fetchCharacterName = async () => {
  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`Failed to fetch data. Status: ${response.status}`);
    }
    const data = await response.json();
    const characterName = data.name;
    console.log(characterName);
    const header = $('#character');
    header.html('<p>' + characterName + '</p>');
    document.getElementById('characterName').innerText = `Character Name: ${characterName}`;
  } catch (error) {
    console.error('Error:', error.message);
  }
};
fetchCharacterName();
