#!/usr/bin/env node
// This script prints two arguments in the format " is "

// Check the number of arguments
const numArgs = process.argv.length - 2;

// If exactly two arguments are passed
if (numArgs === 2)
{
  const argument1 = process.argv[2];
  const argument2 = process.argv[3];
  console.log(argument1, "is", argument2);
}
// If fewer than two arguments are passed
else if (numArgs === 1)
{
	const argument1 = process.argv[2]
	const argument2 = 'undefined';
	console.log(argument1, "is", argument2);
}
else
{
  console.log("undefined is undefined");
}
