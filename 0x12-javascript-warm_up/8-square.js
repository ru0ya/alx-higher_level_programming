#!/usr/bin/node
const sizeArg = process.argv[2];

if (/^\d+$/.test(sizeArg)) {
  const size = parseInt(sizeArg, 10);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
