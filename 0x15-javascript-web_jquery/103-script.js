#!/usr/bin/node
$(document).ready(function () {
  $('INPUT#language_code').on('keydown', function (event) {
    if (event.which === 13) {
      const language = $('#language_code').val();
      const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;

      const fetchHello = async () => {
        try {
          const response = await fetch(apiUrl);

          if (!response.ok) {
            throw new Error(`Failed to fetch data. Status: ${response.status}`);
          }
          const data = await response.json();
          const hello = data.hello;
          const div = $('DIV#hello');
          div.html('<p>' + hello + '</p>');
        } catch (error) {
          console.error('Error:', error.message);
        }
      };
      fetchHello();
    }
  });
});
