#!/usr/bin/node
const factorial = num => {
  if (isNaN(num)) {
    return 1;
  } else if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

const numArg = process.argv[2];
const num = parseInt(numArg, 10);

console.log(factorial(num));
