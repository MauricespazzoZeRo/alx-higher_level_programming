#!/usr/bin/env node
// Script that prints a number converted to integer

const numArgs = process.argv.length - 2;

// If at least one argument is passed
if (numArgs >= 1)
{
	const input = process.argv[2]
	const integerValue = parseInt(input);

	// Check if conversion is possible and result is a number
	if (!isNaN(integerValue))
	{
		console.log("My number:", integerValue);
	}
	else
	{
		console.log("Not a number");
	}
}
// If no arguments are passed
else
{
	console.log("Not a number");
}
