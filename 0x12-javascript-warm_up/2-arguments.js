#!/usr/bin/node
switch (process.argv.length) {
	case 1:
		console.log("No argument");
		break;
	case 2:
		console.log("Argument found");
		break;
	default:
		console.log("Arguments found");
		break;
}
