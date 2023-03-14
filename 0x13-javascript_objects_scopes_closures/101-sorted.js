#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};
for (const x in dict) {
  sortedDict[dict[x]] = [];
}
for (const x in dict) {
  sortedDict[dict[x]].push(x);
}

console.log(sortedDict);
