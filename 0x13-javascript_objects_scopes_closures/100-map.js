#!/usr/bin/node
const initialList = require('./100-data').list;
console.log(initialList);
console.log(initialList.map((elem, i) => elem * i));
