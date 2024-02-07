#!/usr/bin/node
const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

const fetchHello = async () => {
  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`Failed to fetch data. Status: ${response.status}`);
    }
    const data = await response.json();
    const hello = data.hello;
    const div = $('DIV#hello');
    const item = '<p>' + hello + '</p>';
    div.html(item);
  } catch (error) {
    console.error('Error:', error.message);
  }
};
fetchHello();
