#!/usr/bin/node

const request = require('request');
const API_URL = `${process.argv[2]}`;

request({ url: API_URL, json: true }, function (err, resp, body) {
  if (!err) {
    const taskObj = {};
    let completedTask = 0;
    let currentId = 1;

    body.forEach(({ userId, completed }) => {
      taskObj[userId] = completedTask;
      if (currentId === userId) {
        if (completed) { taskObj[userId] = ++completedTask; }
      } else {
        completedTask = 0;
      }
      currentId = userId;
    });
    console.log(taskObj);
  }
});
