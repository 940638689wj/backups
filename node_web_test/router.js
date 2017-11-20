function route(handle, pathname, response) {
	console.log('about to route a request form ' + pathname)
	console.log(handle['/second'])
	console.log(typeof handle['/second'])
	if(typeof handle[pathname] === 'function') {
		handle[pathname](response);
	} else {
		console.log('no request handler');
		response.writeHead(404, {'Content-Type':'text/plain'});
		response.write('404 not found');
		response.end();
	}
}
exports.route = route
