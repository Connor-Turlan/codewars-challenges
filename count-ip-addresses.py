def ips_between(a, b):
    f = lambda g: sum([int(n) * (256 ** (3 - i)) for i, n in enumerate(g)])
    return sum([f(b.split('.')), -f(a.split('.'))])