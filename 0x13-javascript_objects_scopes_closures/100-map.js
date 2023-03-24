#!/usr/bin/node
const initialList = require('./100-data').list;
const newList = initialList.map((elem, i) => elem * i);
console.log(initialList);
console.log(newList);
