#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');

const file_to_read = process.argv[2];

fs.readFile(file_to_read, 'utf-8', (err, data) => {
  if (err) {
    console.error(error);
  } else {
    console.log(data);
  }
});
