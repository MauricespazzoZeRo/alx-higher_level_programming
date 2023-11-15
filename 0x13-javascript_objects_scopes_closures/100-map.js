#!/usr/bin/node
const { list } = require('./100-data');

// Use the map method to create a new array with each value multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial and new arrays
console.log("Initial List:", list);
console.log("New List:", newList);
