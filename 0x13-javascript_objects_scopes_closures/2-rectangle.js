#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof w === 'number' && w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
