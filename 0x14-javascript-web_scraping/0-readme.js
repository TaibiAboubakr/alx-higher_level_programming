#!/usr/bin/node
const fs = require('fs');

const FileName = process.argv.slice(2)[0];
console.log(FileName);

fs.readFile(FileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
