#!/usr/bin/node
const myArg = process.argv[2];

if (/^-?\d+$/.test(myArg)) {
  const num = parseInt(myArg, 10);
  console.log('My number: ${num}');
} else {
  console.log('Not a number');
}
