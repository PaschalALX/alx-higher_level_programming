#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];

request({ url: API_URL, json: true }, function (error, resp, body) {
  if (!error) {
    const results = body.results;
    let num = 0;
    const pattern = /https:\/\/swapi-api.alx-tools.com\/api\/people\/18\/$/;
    for (const { characters } of results) {
      for (const character of characters) {
        if (pattern.test(character)) { num++; }
      }
    }
    console.log(num);
  }
});
