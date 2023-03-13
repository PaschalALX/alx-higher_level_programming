#!/usr/bin/node
const { argv } = process;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  console.log(a + b);
}
if (isNaN(a)) {
  console.log(a);
} else if (isNaN(b)) {
  console.log(b);
} else {
  add(a, b);
}
