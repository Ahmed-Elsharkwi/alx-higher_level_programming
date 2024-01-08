#!/usr/bin/node
const args = process.argv;
const arg = parseInt(args[2], 10);
if (Number.isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
