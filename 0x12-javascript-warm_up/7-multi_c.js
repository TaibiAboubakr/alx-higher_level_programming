#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs === 0) { console.log('Missing number of occurrences'); } else {
  if (!isNaN(process.argv[2])) {
    const x = parseInt(process.argv[2], 10);
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Not a number');
  }
}
