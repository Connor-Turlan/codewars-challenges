const lastDigit = (a, b) => {
	// x ^ 0 == 1;
	if (b === "0") return 1;

	// convert base and power from a, b.
	[base, power] = [
		parseInt(a[a.length - 1]),
		parseInt(b.slice(b.length - 3, b.length)) % 4 || 4,
	];

	// calculate the result, a^b mod 10
	let result = base;
	while (--power > 0) result = (result * base) % 10;
	return result;
};
