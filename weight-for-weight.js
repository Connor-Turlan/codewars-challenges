function sumDigits(n) {
	return n.split("").reduce((sum, d) => sum + parseInt(d), 0);
}

function numberWeightSort(a, b) {
	return sumDigits(a) - sumDigits(b);
}

function orderWeight(s) {
	return s.split(" ").sort().sort(numberWeightSort).join(" ");
}
