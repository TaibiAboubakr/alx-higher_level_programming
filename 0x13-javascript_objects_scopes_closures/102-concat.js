#!/usr/bin/node
const fs = require('fs');
let data = '';
try {
  const fileAContent = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(fileAContent);
  data += fileAContent;
} catch (error) {
  console.error('Error reading the file:', error.message);
}
try {
  const fileBContent = fs.readFileSync(process.argv[3], 'utf-8');
  data += fileBContent;
} catch (error) {
  console.error('Error reading the file:', error.message);
}

try {
  fs.writeFileSync(process.argv[4], data, 'utf-8');
} catch (error) {
  console.error('Error writing to the file:', error.message);
}

try {
  const fileCContent = fs.readFileSync(process.argv[4], 'utf-8');
  console.log(fileCContent);
} catch (error) {
  console.error('Error reading the file:', error.message);
}
