#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs > 0) {
  const n = Number(process.argv[2]);
  function factorial (n) {
    if (isNaN(n) || n === 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  console.log(factorial(n));
}
