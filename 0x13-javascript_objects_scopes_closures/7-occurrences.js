#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  // Use the reduce function to iterate over the elements in the list and accumulate the count
  return list.reduce((count, element) => {
    // For each element, check if it is equal to the searchElement
    if (element === searchElement) {
      // If it is equal, increment the count
      return count + 1;
    } else {
      // If it is not equal, keep the count unchanged
      return count;
    }
  }, 0); // Initialize the count to 0
};
