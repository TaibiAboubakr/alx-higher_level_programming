#!/usr/bin/node
const nArgs = process.argv.length - 2;
const indf = 'is undefined';
if (nArgs === 0) { console.log('undefined is undefined'); } else if (nArgs === 1) { console.log(process.argv[2] + ' ' + indf); } else { console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]); }
