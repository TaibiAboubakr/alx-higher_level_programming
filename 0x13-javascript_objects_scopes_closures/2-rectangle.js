#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  set width (newWidth) {
    this.height = this.validateDimension(newWidth);
  }

  get width () {
    return this.width;
  }

  get height () {
    return this.height;
  }

  set height (newHeight) {
    this.height = this.validateDimension(newHeight);
  }

  validateDimension (value) {
    if (typeof value === 'number' && value > 0) {
      return value;
    } else {
      return {};
    }
  }
};
