def _tribonacci(n, cache):
	if n < len(cache):
		return cache[n]
	else:
		cache.append(_tribonacci(n-3, cache) + _tribonacci(n-2, cache) + _tribonacci(n-1, cache))
		return cache[n]


def tribonacci(signature, n):
	if n == 0:
		return []
    
	_tribonacci(n, signature)
	return signature[:n]