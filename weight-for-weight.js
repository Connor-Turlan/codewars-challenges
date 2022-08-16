const sumDigits = (n) => n.split("").reduce((sum, d) => sum + parseInt(d), 0);

const weightSort = (a, b) => {
	const [A, B] = [sumDigits(a), sumDigits(b)];
	return A === B ? a.localeCompare(b) : A - B;
};

function orderWeight(s) {
	return s.split(" ").sort(weightSort).join(" ");
}
