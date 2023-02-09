#!/usr/bin/node
// writes a string to a file

const fs = require('fs');

const path_to_file = process.argv[2];
const text_to_write = process.argv[3];

fs.writeFile(path_to_file, text_to_write, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
