// takes: String; returns: [ [String,Int] ] (Strings in return value are single characters)
function frequencies(s) {
	return Object.entries(
		s.split("").reduce((counts, char) => {
			char in counts ? counts[char]++ : (counts[char] = 1);
			return counts;
		}, {})
	);
}

// build a huffman tree.
function buildTree(freqs) {
	const tree = freqs.map((entry) => {
		return { type: "leaf", char: entry[0], count: entry[1] };
	});
	while (tree.length > 1) {
		tree.sort((a, b) => a.count - b.count);
		const smallest = tree.splice(0, 2);
		const node = {
			type: "node",
			count: smallest.reduce((sum, node) => sum + node.count, 0),
			left: smallest[0],
			right: smallest[1],
		};
		tree.push(node);
	}
	return tree[0];
}

function buildMap(tree, string = "") {
	if (tree.type === "leaf") return { [tree.char]: string };
	else {
		let node = {};
		if (tree.left) node = { ...buildMap(tree.left, string + "0") };
		if (tree.right)
			node = { ...node, ...buildMap(tree.right, string + "1") };
		return node;
	}
}

// takes: [ [String,Int] ], String; returns: String (with "0" and "1")
function encode(freqs, s) {
	if (freqs.length <= 1) return null;

	const huffmanMap = buildMap(buildTree(freqs));
	return s
		.split("")
		.map((char) => huffmanMap[char])
		.join("");
}

// takes [ [String, Int] ], String (with "0" and "1"); returns: String
function decode(freqs, bits) {
	if (freqs.length <= 1) return null;

	const root = buildTree(freqs);
	let node = root;
	return bits.split("").reduce((string, bit) => {
		node = bit === "0" ? node.left : node.right;
		if (node.type === "leaf") {
			string += node.char;
			node = root;
		}
		return string;
	}, "");
}
