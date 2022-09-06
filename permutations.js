// swap two elements in an array.
function swap(arr, i, j) {
	[arr[i], arr[j]] = [arr[j], arr[i]];
}

// reverse an array. supports subindexing.
function reverse(arr, i, j) {
	let k = 0;
	while (i + k < j - k) {
		swap(arr, i + k, j - k);
		k++;
	}
}

// find largest index that satisfies a[k] < a[k + 1].
function findK(arr) {
	let k = -1;
	for (let i = 0; i < arr.length - 1; i++) {
		if (arr[i] < arr[i + 1]) {
			k = i;
		}
	}
	return k;
}

// find largest index that satisfies a[k] < a[l].
function findL(arr, k) {
	let l = k;
	for (let i = k + 1; i < arr.length; i++) {
		if (arr[k] < arr[i]) {
			l = i;
		}
	}
	return l;
}

function permute(inputString) {
	const permutations = [];
	const array = [...inputString.split("")];

	// k will be >0 while there are still valid permutations remaining.
	let k = findK(array);
	while (k > -1) {
		//output the permutation.
		permutations.push(array.join(""));

		// find the next permutation.
		let l = findL(array, k);
		swap(array, k, l);
		reverse(array, k + 1, array.length - 1);
		k = findK(array);
	}
	//output the permutation.
	permutations.push(array.join(""));
	return permutations;
}

function permutations(string) {
	return permute(string.sort());
}
