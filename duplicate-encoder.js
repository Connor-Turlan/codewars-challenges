function duplicateEncode(word) {
	// get the char counts.
	const counts = word
		.toLowerCase()
		.split("")
		.reduce((counts, c) => {
			c in counts ? counts[c]++ : (counts[c] = 1);
			return counts;
		}, {});

	// remap the word with '(' for single chars and ')' for duplicates.
	return word
		.toLowerCase()
		.split("")
		.map((char) => (counts[char] > 1 ? ")" : "("))
		.join("");
}
