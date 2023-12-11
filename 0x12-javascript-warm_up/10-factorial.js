#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs > 0 && !isNaN(process.argv[2])) {
  const n = parseInt(process.argv[2], 10);
  const computeFactorial = (n) => {
    if (isNaN(n)) {
      return 1;
    } else if (n <= 1) {
      return 1;
    } else {
      return n * computeFactorial(n - 1);
    }
  };
  console.log(computeFactorial(n));
} else {
  console.log('NaN');
}
