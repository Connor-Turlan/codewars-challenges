def getScore(n, count):
	score = 0

	if count >= 3:
		score += 1000 if n == 1 else n * 100
		count -= 3
		
	if n == 1:
		score += count * 100
	elif n == 5:
		score += count * 50

	return score

def score(dice):
	counts = [dice.count(i + 1) for i in range(6)]
	scores = [getScore(i + 1, count) for i, count in enumerate(counts)]
	return sum(scores)