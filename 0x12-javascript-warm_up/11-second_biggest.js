#!/usr/bin/node
const { argv } = process;
const argc = argv.length;

if (argc <= 3) {
  console.log(0);
} else {
  const mainArgv = argv.slice(2).map((val) => parseInt(val));
  mainArgv.sort((a, b) => b - a);
  console.log(mainArgv[1]);
}
