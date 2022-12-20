#!/usr/bin/node
const add = (a, b) => a + b;

const firstArg = process.argv[2];
const secondArg = process.argv[3];

if (/^-?\d+$/.test(firstArg) && /^-?\d+$/.test(secondArg)) {
  const num1 = parseInt(firstArg, 10);
  const num2 = parseInt(secondArg, 10);
  console.log(add(num1, num2));
} else {
  console.log('Error: Arguments must be integers');
}
