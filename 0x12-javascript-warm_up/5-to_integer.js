#!/usr/bin/node
const args = process.argv;
const arg = parseInt(args[2], 10);
if (Number.isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
