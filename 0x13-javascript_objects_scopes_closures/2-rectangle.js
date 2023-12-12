#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this._width = w;
    this._height = h;
  }

  set width (newWidth) {
    this._height = this.validateDimension(newWidth);
  }

  get width () {
    return this._width;
  }

  get height () {
    return this._height;
  }

  set height (newHeight) {
    this._height = this.validateDimension(newHeight);
  }

  validateDimension (value) {
    if (typeof value === 'number' && value > 0) {
      return value;
    } else {
      return {};
    }
  }
};
