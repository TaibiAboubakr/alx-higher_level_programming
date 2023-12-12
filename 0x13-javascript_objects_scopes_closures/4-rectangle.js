#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof w === 'number' && w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { result += 'X'; }
      if (i < this.height - 1) { result += '\n'; }
    }
    console.log(result);
  }

  rotate () {
    const t = this.height;
    this.height = this.width;
    this.width = t;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
