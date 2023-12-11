#!/usr/bin/node
const nArgs = process.argv.length - 1;
if (nArgs > 2) {
  let max = parseInt(process.argv[2], 10);

  for (let i = 3; i <= nArgs; i++) {
    const Num = parseInt(process.argv[i], 10);
    if (!isNaN(Num) && Num > max) {
      max = Num;
    }
  }
  let secondMax = parseInt(process.argv[2], 10);
  for (let i = 3; i <= nArgs; i++) {
    const Num = parseInt(process.argv[i], 10);
    if (!isNaN(Num) && Num > secondMax && Num < max) {
      secondMax = Num;
    }
  }
  console.log(secondMax);
} else {
  console.log('0');
}
