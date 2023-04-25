#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const options = {
  url,
  json: true
};

request(options, function (error, resp, body) {
  if (!error) {
    const movieTitle = body.title;
    console.log(movieTitle);
  }
});
