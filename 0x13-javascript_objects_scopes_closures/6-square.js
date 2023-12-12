#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c = 'X') {
    let result = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) { result += c; }
      if (i < this.width - 1) { result += '\n'; }
    }
    console.log(result);
  }
};
