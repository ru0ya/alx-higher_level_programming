#!/usr/bin/node
/**
 * create a constant variable `num` and assign the second arg to it
 * convert the second arg to Number
 * if it throws NaN error, print out `Not a number`
 */
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
