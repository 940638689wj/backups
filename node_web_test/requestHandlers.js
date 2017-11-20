var exec = require('child_process').exec;

function start(response) {
	console.log('start was called');

	exec('c: && dir /ad/s/b',{timeout:10000, maxBuffer:20000*1024}, function(error, stdout, stderr) {
		response.writeHead(200, {'Content-Type':'text/plain;charset=gbk'});
		response.write(stdout);
		response.end();
	});
}

function second(response) {
	console.log('second was called');

	exec('c: && dir /ad/s/b',{timeout:20000, maxBuffer:20000*1024}, function(error, stdout, stderr) {
		response.writeHead(200, {'Content-Type':'text/plain;charset=gbk'});
		response.write(stdout);
		response.end();
	});
}


function upload(response) {
	console.log('start was called');
	response.writeHead(200, {'Content-Type':'text/plain'});
	response.write('hello upload');
	response.end();
}

exports.start = start;
exports.second   = second;
exports.upload = upload;