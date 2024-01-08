#!/usr/bin/node
const args = process.argv;
const arg = parseInt(args[2], 10);
if (Number.isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
