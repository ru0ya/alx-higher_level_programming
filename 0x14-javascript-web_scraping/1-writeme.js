#!/usr/bin/node
// writes a string to a file

const fs = require('fs');

const pathToFile = process.argv[2];
const textToWrite = process.argv[3];

fs.writeFile(pathToFile, textToWrite, 'utf-8', function (err) {
  if (err) {
    console.error(err);
  }
});
