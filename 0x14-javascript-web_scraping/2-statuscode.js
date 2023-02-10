#!/usr/bin/node
// displays GET request status code

const request = require('request');

const url_to_request = process.argv[2];

request.get(url_to_request, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
