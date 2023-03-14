#!/usr/bin/node
const initialList = require('./100-data').list;
const newList = initialList.map((elem, i) => elem * 1));
console.log(initialList);
console.log(newList);
