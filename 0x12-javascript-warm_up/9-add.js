#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const args = process.argv;
const first = parseInt(args[2], 10);
const second = parseInt(args[3], 10);
console.log(add(first, second));
