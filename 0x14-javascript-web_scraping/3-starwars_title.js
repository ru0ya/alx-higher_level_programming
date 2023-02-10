#!/usr/bin/node
// prints the title of a star wars movie
// where episode number matches given int

const request = require('request');

const toUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(toUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
	  const movie = JSON.parse(body);
	  console.log(movie.title);
  }
});
