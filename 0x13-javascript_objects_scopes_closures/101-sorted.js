#!/usr/bin/node
const { dict } = require('./101-data');
const newdict = {};
for (const key in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, key)) {
    const value = dict[key];
    if (value in newdict) {
      newdict[value].push(key);
    } else {
      newdict[value] = [key];
    }
  }
}
console.log(newdict);
