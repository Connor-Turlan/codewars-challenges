function smolmul(a, b) {
	let A = parseInt(a);
	let B = parseInt(b);
	return (A * B).toString();
}

function karatsuba(a, b) {
	//swap inputs if b > a.
	if (a.length < b.length) {
		return karatsuba(b, a);
	}

	// base case is three digit multiplication.
	// get the midpoint of the smaller number.
	// split the number on the midpoint.
	// do karatsuba.
	// raise numbers to their original power.
	// return the result.
}

function trimLeadingZeroes(n) {
	return n.split("").reduce((s, c) => (s || c ? s + c : s), "");
}

function multiply(a, b) {
	a = trimLeadingZeroes(a);
	b = trimLeadingZeroes(b);
	return smolmul(a, b);
}
