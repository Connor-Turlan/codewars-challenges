function solution(list) {
	return (
		list
			// get the differences between each element in the array.
			.map((n, i, arr) => {
				return { n, diff: (arr[i - 1] || 0) - n };
			})

			// produce an array split when the difference is greater that |1| and differs from the previous.
			.reduce(
				(ranges, n) => {
					const prev = ranges[0];
					if (
						n.diff ** 2 !== 1 &&
						prev[prev.length - 1] &&
						n.diff !== prev[prev.length - 1].diff
					) {
						ranges.unshift([n.n]);
					} else {
						prev.push(n.n);
					}
					return ranges;
				},
				[[]]
			)

			// reduce the array ranges.
			.map((range) =>
				range.length > 2
					? [range.shift(), range.pop()].join("-")
					: range.join(",")
			)

			// reverse the array, as we unshifted new values.
			.reverse()

			// join the array series.
			.join(",")
	);
}
