def anagrams(word, words):
    sort = lambda s: ''.join(sorted(s, key=str.lower))
    return [w for w in words if sort(w) == sort(word)]