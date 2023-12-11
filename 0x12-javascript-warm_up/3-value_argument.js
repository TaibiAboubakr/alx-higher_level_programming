#!/usr/bin/node
const nArgs = process.argv.length - 2;
if (nArgs === 0) { console.log('No argument'); } else { console.log(process.argv[2]); }
