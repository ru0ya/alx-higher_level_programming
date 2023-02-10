#!/usr/bin/node
// computes number fo completed tasks
// in given url

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasksCompleted = {};
    const data = JSON.parse(body);
    data.forEach((todo) => {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    });
    console.log(tasksCompleted);
  }
});
