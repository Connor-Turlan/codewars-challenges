function findOdd(A) {
	return parseInt(
		Object.entries(
			A.reduce((counts, item) => {
				if (item in counts) counts[item]++;
				else counts[item] = 1;
				return counts;
			}, {})
		).find((entry) => entry[1] % 2)[0]
	);
}
