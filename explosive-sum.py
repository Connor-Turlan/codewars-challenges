""" def exp_sum(n):
    sum = 1
    for i in range(1, n):
        half = n / 2
        sum += half - abs(i - half)
    return sum """

def exp_sum(n): 
	problem_space = [1 for i in range(n+1)]
	for i in range(2, n+1): 
		for j in range(i, n+1): problem_space[j] += problem_space[j-i]
	return problem_space[-1]

[print(exp_sum(n)) for n in range(1, 11)]