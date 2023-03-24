#!/usr/bin/node
const { argv } = process;
const num = parseInt(argv[2]);

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  if (num < 1) {
    return 0;
  }
  return num * factorial(num - 1);
}

console.log(factorial(num));
