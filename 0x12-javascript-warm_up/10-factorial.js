#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs > 0 && !isNaN(process.argv[2])) {
  const n = Number(process.argv[2]);
  function factorial (n) {
    if (isNaN(n)) {
      return 1;
    } else if (n === 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  console.log(factorial(n));
}
