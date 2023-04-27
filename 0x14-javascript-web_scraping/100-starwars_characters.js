#!/usr/bin/node
const request = require('request');

const FILM_ID = process.argv[2];
const FILM_API_URL = `https://swapi-api.alx-tools.com/api/films/${FILM_ID}`;

request({ url: FILM_API_URL, json: true }, (err, resp, body) => {
  if (!err) {
    const charactersURLs = body.characters;

    charactersURLs.forEach((xterURL) => {
      request({ url: xterURL, json: true }, (err, resp, body) => {
        if (!err) console.log(body.name);
      });
    });
  }
});
