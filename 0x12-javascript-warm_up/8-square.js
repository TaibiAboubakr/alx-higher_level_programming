#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs > 0 && !isNaN(process.argv[2])) {
  const x = parseInt(process.argv[2], 10);
  let result = '';
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) { result += 'X'; }
    if (i < x - 1) { result += '\n'; }
  }
  console.log(result);
} else {
  console.log('Missing size');
}
