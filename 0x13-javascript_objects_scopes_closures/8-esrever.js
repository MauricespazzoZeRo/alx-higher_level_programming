#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];

  // Iterate over the input list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
