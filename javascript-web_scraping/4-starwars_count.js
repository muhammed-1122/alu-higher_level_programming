#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const count = data.results.filter(film =>
      film.characters.some(char => char.includes('/18/'))
    ).length;
    console.log(count);
  }
});
