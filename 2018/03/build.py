from functools import reduce
from operator import mul

def gen_primes(n):
    primes = [2]
    for i in range(3, n+1, 2):
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes

def is_too_large(factors):
    return reduce(mul, factors) > 2**32

def build_juletall():
    primes = gen_primes(2**10)
    idx = [0] * 24
    juletall = 0
    while True:
        pos = 0
        factors = [primes[i] for i in idx]
        while is_too_large(factors):
            pos += 1
            if pos > 13:
                return juletall
            idx[:pos+1] = [idx[pos] + 1] * len(idx[:pos+1])
            factors = [primes[i] for i in idx]
        juletall += 1
        idx[0] += 1

print(build_juletall())
# Svar: 914


