#!/usr/bin/node
const request = require('request');

const FILM_ID = process.argv[2];
const FILM_API_URL = `https://swapi-api.alx-tools.com/api/films/${FILM_ID}`;

const getCharacterNames = (URLs, URLsLen, ptr = 0) => {
  if (ptr === URLsLen) return;

  request({ url: URLs[ptr], json: true }, (err, resp, body) => {
    if (!err) {
      getCharacterNames(URLs, URLsLen, ptr + 1);
      console.log(body.name);
    }
  });
};
request({ url: FILM_API_URL, json: true }, (err, resp, body) => {
  if (!err) {
    const charactersURLs = body.characters;
    const charactersURLsLen = charactersURLs.length;
    getCharacterNames(charactersURLs, charactersURLsLen);
  }
});
