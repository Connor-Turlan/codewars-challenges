import string

def substitute(char, offset, cipherspace):
	if char in cipherspace:
		return cipherspace[(cipherspace.index(char) + offset) % len(cipherspace)]
	return char

def rot13(m):
	m = ''.join([substitute(c, 13, string.ascii_uppercase) for c in m])
	return ''.join([substitute(c, 13, string.ascii_lowercase) for c in m])
