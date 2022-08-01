import copy

cached_counters = {}
cached_swaps = {}


def build_from_cache(string, order):
    newstr = [""] * len(string)
    for i, char in enumerate(string):
        newstr[i] = string[order[i]]
    return "".join(newstr)


def check_cache(s, n):    
    # check if the string length is already in the length.
    if len(s) not in cached_counters:
        return False, None
    
    sl = len(s)
    n %= cached_counters[sl]
    if n >= len(cached_swaps[sl]):
        end = len(cached_swaps[sl])
        newstr = build_from_cache(s, cached_swaps[sl][-1])
        string, order_results = _jumbled_string(newstr, n-end+1, cached_swaps[sl][-1])
        cached_swaps[sl].extend(order_results[1:])
        return True, string
        return False, None
    
    if sl in cached_swaps:
        string = build_from_cache(s, cached_swaps[sl][n])
    else:
        string, = _jumbled_string(s, n)
    return True, string


def cache_results(s, magic_n, results):    
    cached_counters[len(s)] = magic_n
        
    # store the chain of swaps.
    sl = len(s)
    if sl not in cached_swaps:
        cached_swaps[sl] = results
    else:
        if len(cached_swaps[sl]) < len(results):
            cached_swaps[sl] = results
    

def _jumbled_string(s, n, curr_order=[]):
    magic_counter = 0
    repeat_found = False
    results = [s]
    order = curr_order if len(curr_order) > 0 else [i for i in range(len(s))]
    order_results = [[copy.deepcopy(order)]]
    
    if n <= 0:
        return s, order_results
    
    inCache, result = check_cache(s, n)
    if inCache and len(curr_order) == 0:
        print("cache hit!")
        return result, order_results

    i = 0
    while i < n:
        strings = ["", ""]
        arrays = [[], []]
        j = 0
        while j < len(s):
            strings[j % 2] += s[j]
            arrays[j % 2].append(order[j])
            j += 1
            
        s = "".join(strings)
        results.append(s)
        order = arrays[0]
        order.extend(arrays[1])
        order_results.append(copy.deepcopy(order))

        repeat_found = s == results[0]
        
        magic_counter += 1
        if repeat_found:
            cache_results(s, magic_counter, order_results)
            return results[n % magic_counter], order_results
        i += 1

    cache_results(s, 9999, order_results)
    return s, order_results

def jumbled_string(s, n):
    return _jumbled_string(s, n)[0]