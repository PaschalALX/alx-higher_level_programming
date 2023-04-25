#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const API_URL = process.argv[2];
const FILE_PATH = process.argv[3];

request(API_URL, function (error, resp, body) {
  if (!error) { fs.writeFileSync(FILE_PATH, body, 'utf-8'); } else { console.log(error); }
});
