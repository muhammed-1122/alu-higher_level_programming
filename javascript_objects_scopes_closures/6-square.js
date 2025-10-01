#!/usr/bin/node
const Square0 = require('./5-square');

module.exports = class Square extends Square0 {
  charPrint(c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};

