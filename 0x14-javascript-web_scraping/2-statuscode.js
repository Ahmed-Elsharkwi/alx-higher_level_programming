#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, res) {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  console.log('code:', res.statusCode);
});
