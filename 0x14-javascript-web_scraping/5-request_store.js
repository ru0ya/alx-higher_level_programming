#!/usr/bin/node
// gets content of a webpage and
// stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileStorage = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fileStorage, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
