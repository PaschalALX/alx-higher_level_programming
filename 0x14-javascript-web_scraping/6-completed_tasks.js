#!/usr/bin/node

const request = require('request');
const API_URL = `${process.argv[2]}`;

request({ url: API_URL, json: true }, function (err, resp, body) {
  if (!err) {
    const completedTaskByUsers = {};

    body.forEach(({ userId, completed }) => {
      if (completed && !completedTaskByUsers[userId]) completedTaskByUsers[userId] = 0;
      if (completed) completedTaskByUsers[userId]++;
    });
    console.log(completedTaskByUsers);
  }
});
