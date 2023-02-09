#!/usr/bin/node
// displays GET request status code

const request = require('request');

const url_to_request = process.argv[2];

request(url_to_request, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log('code: ${response.statusCode}');
});
