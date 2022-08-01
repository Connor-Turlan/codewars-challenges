import copy

cached_swaps = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 4, 7: 3, 8: 3, 9: 6, 10: 6, 12: 10, 14: 12, 16: 4, 18: 8, 20: 18, 22: 6, 24: 11, 26: 20, 28: 18, 30: 28, 32: 5, 34: 10, 36: 12, 38: 36, 40: 12, 42: 20, 44: 14, 46: 12, 48: 23, 50: 21, 52: 8, 54: 52, 56: 20, 58: 18, 60: 58, 62: 60, 64: 6, 66: 12, 68: 66, 70: 22, 72: 35, 74: 9, 76: 20, 78: 30, 80: 39, 82: 54, 84: 82, 86: 8, 88: 28, 90: 11, 92: 12, 94: 10, 96: 36, 98: 48, 100: 30, 102: 100, 104: 51, 106: 12, 110: 36, 112: 36, 114: 28, 116: 44, 118: 12, 120: 24, 124: 20, 126: 100, 128: 7, 130: 14, 134: 18, 136: 36, 138: 68, 142: 46, 144: 60, 146: 28, 148: 42, 152: 15, 154: 24, 156: 20, 158: 52, 160: 52, 162: 33, 166: 20, 168: 83, 172: 18, 176: 60, 178: 58, 184: 60, 186: 36, 188: 40, 11: 10, 13: 12, 15: 4, 17: 8, 19: 18, 21: 6, 23: 11, 25: 20, 27: 18, 29: 28, 31: 5, 33: 10, 35: 12, 37: 36, 39: 12, 41: 20, 43: 14, 45: 12, 47: 23, 49: 21, 51: 8, 53: 52, 55: 20, 57: 18, 59: 58, 61: 60, 63: 6, 65: 12, 67: 66, 69: 22, 71: 35, 73: 9, 75: 20, 77: 30, 79: 39, 81: 54, 83: 82, 85: 8, 87: 28, 89: 11, 91: 12, 93: 10, 95: 36, 97: 48, 99: 30}

def faro_length(l):
    N = (2 * l) + 1
    A, K, result = 2, 0, 1
    i = 0
    while K < l:
        result = (result * A) % N
        if result == 1:
            return K

        K += 1
    return 0

def jumbled_cache(history, string, n):
    return ''.join([string[i] for i in history[n]])

def jumbled_string(s, n):
    history = [s]

    if len(s) in cached_swaps:
        n %= cached_swaps[len(s)]
        """ if len(cached_swaps[len(s)]) < n:
            return jumbled_cache(cached_swaps[len(s)], s, n)
        else:
            pass """

    i = 0   
    while i < n:
        halves = ['', '']
        for j, char in enumerate(s):
            halves[j%2] += char
        s = ''.join(halves)
        i += 1
        if s == history[0]:
            cached_swaps[len(s)] = i
            #cached_swaps[len(s)] = history
            print(i)
            return history[n % len(history)]
        history.append(s)
    return s

for i in range(1, 100):
    string = ''.join([chr(j) for j in range(i)])
    print(i, end=':\t')

    print(f"faro:\t%d" % faro_length(len(string)))
    jumbled_string(string, 100)

print(cached_swaps)

# final solution.
cached_swaps = {}#{0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 4, 7: 3, 8: 3, 9: 6, 10: 6, 12: 10, 14: 12, 16: 4, 18: 8, 20: 18, 22: 6, 24: 11, 26: 20, 28: 18, 30: 28, 32: 5, 34: 10, 36: 12, 38: 36, 40: 12, 42: 20, 44: 14, 46: 12, 48: 23, 50: 21, 52: 8, 54: 52, 56: 20, 58: 18, 60: 58, 62: 60, 64: 6, 66: 12, 68: 66, 70: 22, 72: 35, 74: 9, 76: 20, 78: 30, 80: 39, 82: 54, 84: 82, 86: 8, 88: 28, 90: 11, 92: 12, 94: 10, 96: 36, 98: 48, 100: 30, 102: 100, 104: 51, 106: 12, 110: 36, 112: 36, 114: 28, 116: 44, 118: 12, 120: 24, 124: 20, 126: 100, 128: 7, 130: 14, 134: 18, 136: 36, 138: 68, 142: 46, 144: 60, 146: 28, 148: 42, 152: 15, 154: 24, 156: 20, 158: 52, 160: 52, 162: 33, 166: 20, 168: 83, 172: 18, 176: 60, 178: 58, 184: 60, 186: 36, 188: 40, 11: 10, 13: 12, 15: 4, 17: 8, 19: 18, 21: 6, 23: 11, 25: 20, 27: 18, 29: 28, 31: 5, 33: 10, 35: 12, 37: 36, 39: 12, 41: 20, 43: 14, 45: 12, 47: 23, 49: 21, 51: 8, 53: 52, 55: 20, 57: 18, 59: 58, 61: 60, 63: 6, 65: 12, 67: 66, 69: 22, 71: 35, 73: 9, 75: 20, 77: 30, 79: 39, 81: 54, 83: 82, 85: 8, 87: 28, 89: 11, 91: 12, 93: 10, 95: 36, 97: 48, 99: 30}

def jumbled_string(s, n):
    # store a history of swaps for this string.
    history = [s]

    # if we have encountered a string with this length before, mod the n.
    if len(s) in cached_swaps:
        n %= cached_swaps[len(s)]

    # continue swapping until we reach n.
    i = 0   
    while i < n:
        # shift odd chars to the start of the string, even to the end.
        halves = [s[i] for i in range(0, len(s), 2)] + ([s[i] for i in range(1, len(s), 2)])
        s = ''.join(halves)

        s = s[::2] + s[1::2]
        
        # check if the current string is in the history.
        i += 1
        if s == history[0]:
            # if so, cache and return the string.
            cached_swaps[len(s)] = i
            return history[n % len(history)]
        
        # save this history.
        history.append(s)
    
    # return the jumbled string.
    return s