function change_path(child_node_id) {
	fetch("/lectures", {
		method: "POST",
		body: JSON.stringify( {child_node_id: child_node_id} ),
	}).then((_res) => {
		window.location.href = "/lectures";
	});
}