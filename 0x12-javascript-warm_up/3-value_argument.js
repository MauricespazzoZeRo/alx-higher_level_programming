#!/usr/bin/env node
// script that prints a message depending of the number of arguments passed

// Check the number of args
const argsNum = process.argv.length - 2;

// If no args are passed
if (argsNum === 0)
{
	console.log("No argument");
}
// If only one argument is passed
else if (argsNum === 1)
{
	console.log(process.argv[2]);
}
// If more than one argument is passed
else
{
	console.log(process.argv[2]);
}
