function digital_root(n) {
	let root = n
		.toString()
		.split()
		.map((d) => parseInt(d))
		.reduce((sum, d) => sum + d);
	return root < 10 ? root : digital_root(root);
}
