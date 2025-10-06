#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach(task => {
      if (task.completed) {
        if (!completed[task.userId]) {
          completed[task.userId] = 0;
        }
        completed[task.userId]++;
      }
    });

    console.log(completed);
  }
});
