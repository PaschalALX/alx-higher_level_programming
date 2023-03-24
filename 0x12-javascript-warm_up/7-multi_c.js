#!/usr/bin/node
const { argv } = process;
const str = 'C is fun';
const x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
