#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs === 0) { console.log('Not a number'); } else {
  if (!isNaN(process.argv[2])) {
    const argumentAsNumber = parseInt(process.argv[2], 10);
    console.log('My number: ' + argumentAsNumber);
  } else {
    console.log('Not a number');
  }
}
