#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs > 1 && !isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
  const n1 = parseInt(process.argv[2], 10);
  const n2 = parseInt(process.argv[3], 10);
  function add (a, b) {
    return a + b;
  }
  console.log(add(n1, n2));
} else {
  console.log('NaN');
}
