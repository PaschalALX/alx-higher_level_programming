#!/usr/bin/node
const { argv } = process;
const len = argv.length;

if (len === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
