#!/usr/bin/env node
// This script prints the 2 arguments passed to it

// Check the number of arguments
const numArgs = process.argv.length - 2;

// If no arguments are passed
if (numArgs === 0)
{
	console.log("No argument");
}
else if (numArgs === 1)
{
	
}
// If at least one argument is passed
else
{
	// Use slice to get only the arguments (excluding path and executable)
	const argsList = process.argv.slice(2).join(" is ");
	console.log(argsList);
}
