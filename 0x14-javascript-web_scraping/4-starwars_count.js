#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];

request({ url: API_URL, json: true }, function (error, resp, body) {
  if (!error) {
    const results = body.results;
    let num = 0;
    const pattern = /.*\/(?<characterId>[1-9][0-9]*)\/$/;

    for (const { characters } of results) {
      for (const character of characters) {
        const { characterId } = character.match(pattern).groups;
        if (characterId === '18') { num++; }
      }
    }
    console.log(num);
  }
});
