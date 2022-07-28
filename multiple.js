function solution(number) {
	return [...Array(number).keys()]
		.filter((n) => n % 3 === 0 || n % 5 === 0)
		.reduce((sum, n) => sum + n, 0);
}

console.log(solution(10));
