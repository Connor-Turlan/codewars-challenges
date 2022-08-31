import string

def sub(c, offset):
	for cipher in (string.ascii_uppercase, string.ascii_lowercase):
		if c in cipher:
			return cipher[(cipher.index(c) + offset) % len(cipher)]
	return c

def rot13(message):
    return ''.join([sub(c, 13) if c.isalpha() else c for c in message])