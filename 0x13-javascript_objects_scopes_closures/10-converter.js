#!/usr/bin/node
exports.converter = function (base) {
  // Use the built-in toString method to convert the number to the specified base
  return function (number) {
    return number.toString(base);
  };
};
