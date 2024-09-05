#!/usr/bin/node

const request = require('request-promise-native');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

async function getCharacters() {
  try {
    const body = await request(apiUrl);
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const characterData = await request(characterUrl);
      const character = JSON.parse(characterData);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters();

