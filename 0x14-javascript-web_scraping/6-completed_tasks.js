#!/usr/bin/node
const request = require('request');
const newdict = {};
request.get(process.argv[2], function (err, res, body) {
  if (err){
     return;
  }
  const data = JSON.parse(body);
  let count = 0;
  let user_id = data[0].userId;
  for (let i = 0; i < data.length; i++) {
	  if (data[i].completed === true) {
	       if (data[i].userId === user_id) {
		       newdict[data[i].userId] = ++count;
	      } else if (data[i].userId != user_id) {
		       user_id = data[i].userId;
		       count = 1;
		       newdict[data[i].userId] = count;
	  }
    }
  }
  console.log(newdict);
});
