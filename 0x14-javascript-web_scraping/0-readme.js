#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');

const fileToRead = process.argv[2];

fs.readFile(fileToRead, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
