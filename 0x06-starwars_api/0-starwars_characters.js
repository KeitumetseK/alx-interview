#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  let index = 0;

  function printCharacter(characterUrl) {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      index++;
      if (index < characters.length) {
        printCharacter(characters[index]);
      }
    });
  }

  printCharacter(characters[index]);
});

