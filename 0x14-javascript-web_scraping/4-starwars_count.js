#!/usr/bin/node
// prints the number of movies where
// the character is "Wedge Antilles"

const request = require('request');
const url = process.argv[2];
const charId = 18;
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
