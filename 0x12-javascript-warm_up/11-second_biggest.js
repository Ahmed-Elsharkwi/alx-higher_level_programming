#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const arr = args.slice(2).map(Number);
  const num = Math.max.apply(null, arr);
  let number = arr[0];
  for (let j = 1; j < arr.length; j++) {
    if (number < num && number < arr[j]) {
      if (arr[j] !== num) { number = arr[j]; }
    }
  }
  console.log(number);
}
