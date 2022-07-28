cached_counters = {}

def jumbled_string(s, n):
    magic_counter = 0
    original_string = s
    repeat_found = False
    results = [s]
    
    if n <= 0:
        return s
    
    if len(s) in cached_counters:
        n %= cached_counters[len(s)]

    i = 0
    while i < n:
        strings = ["", ""]
        j = 0
        while j < len(s):
            strings[j % 2] += s[j]
            j += 1
            
        s = "".join(strings)
        results.append(s)

        repeat_found = s == original_string
        
        magic_counter += 1
        if repeat_found:
            return results[n % magic_counter]
        i += 1
        
    return s


results = []
for k in range(100):
    for i in range(100):
        string = "".join([str(j) for j in range(k)])
        result = jumbled_string(string, i)

        if result not in results:
            results.append(result)
        else:
            print(k, i-1)
            break

for i in range(10):
    print(jumbled_string("abcd", i))
    print()