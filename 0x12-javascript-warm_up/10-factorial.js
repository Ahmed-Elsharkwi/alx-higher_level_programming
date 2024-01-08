#!/usr/bin/node
function factor (a) {
  if (a === 1) { return (1); }
  const res = a - 1;
  return (a * factor(res));
}
const args = process.argv;
const arg = parseInt(args[2], 10);
if (Number.isNaN(arg)) {
  console.log(1);
} else {
  console.log(factor(arg));
}
