#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    c === undefined ? this.print() : this.print(c);
  }
}
module.exports = Square;
