#!/usr/bin/node
const myArg = process.argv[2];

if (/^\d+$/.test(myArg)) {
  const num = parseInt(myArg, 10);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
