#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let result = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) { result += c; }
      if (i < this.width - 1) { result += '\n'; }
    }
    console.log(result);
  }
};
