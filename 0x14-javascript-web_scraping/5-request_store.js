#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      console.error(err);
    }
  });
});
