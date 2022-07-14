function changePath(node_id) {
	console.log( 1543 );
	fetch("/lectures", {
		method: "POST",
		body: JSON.stringify({ node_id: node_id }),
	}).then((_res) => {
		window.location.href = "/lectures";
	});
}