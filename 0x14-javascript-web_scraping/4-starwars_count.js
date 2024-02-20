#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const list = data.results[i].characters;
    for (let j = 0; j < list.length; j++) {
      if (list[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
