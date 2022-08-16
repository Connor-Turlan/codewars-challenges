function topThreeWords(text) {
	const counts = (text.toLowerCase().match(/[\w]+'?[\w]*/g) || []).reduce(
		(counts, word) => {
			if (word) word in counts ? counts[word]++ : (counts[word] = 1);
			return counts;
		},
		{}
	);
	return Object.entries(counts)
		.sort((a, b) => b[1] - a[1])
		.map((entry) => entry[0])
		.slice(0, 3);
}
