#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const {
      width,
      height
    } = this;
    for (let i = 0; i < height; i++) {
      let concat = '';
      for (let j = 0; j < width; j++) {
        concat += 'X';
      }
      console.log(concat);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
