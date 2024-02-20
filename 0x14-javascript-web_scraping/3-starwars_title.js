#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/?format=json', function (err, res, body) {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
