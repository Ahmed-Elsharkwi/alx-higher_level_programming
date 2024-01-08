// Declare a 2D array
const array = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

// Outer loop
for (let i = 0; i < array.length; i++) {
  // Inner loop
  for (let j = 0; j < array[i].length; j++) {
    // Print the eleme
    process.stdout.write(array[i][j]);
  }
}
// Output: HelloWorld
