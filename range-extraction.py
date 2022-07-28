def solution(args):
	diffs = [
		{
			'n': n, 
			'diff': (args[i-1 if i > 0 else 0] - n) if i > 0 else 0,
		} for i, n in enumerate(args)
	]

	ranges = [[]]
	for n in diffs:
		prev = ranges[-1]
		if n['diff'] ** 2 != 1 and prev and prev[-1] and n['diff'] != prev[-1]['diff']:
			ranges.append([n])
		else:
			prev.append(n)
	
	print(diffs, [n['n'] for n in range for range in ranges])