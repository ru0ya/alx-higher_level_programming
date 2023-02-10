#!/usr/bin/node
// displays GET request status code

const request = require('request');

const urlToRequest = process.argv[2];

request.get(urlToRequest, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
