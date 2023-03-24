#!/usr/bin/node
const { argv } = process;
const x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else if (x > 0) {
  let horin = '';
  for (let i = 0; i < x; i++) {
    horin += 'X';
  }

  for (let i = 0; i < x; i++) {
    console.log(horin);
  }
}
