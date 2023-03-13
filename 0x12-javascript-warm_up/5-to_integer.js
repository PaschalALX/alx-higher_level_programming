#!/usr/bin/node
const { argv } = process;

const number = parseInt(argv[2]);

if (number || number === 0) {
  console.log(number);
} else {
  console.log('Not a number');
}
