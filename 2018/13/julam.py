def gen_primes(n):
    primes = [2]
    for i in range(3, n, 2):
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
            yield i

def find_next(seq):
    i = max(seq)+1
    while True:
        ctr = 0
        for m in seq:
            if i - m in seq and i != 2*m:
                ctr += 1
        if ctr == 2:
            return i
        else:
            i += 1

g = gen_primes(100000) # Burde holde
n = {1, 3}
primes = {2}
included_primes = set()

while True:
    while max(n) >= max(primes):
        primes.add(next(g))
    if max(n) in primes:
        included_primes.add(max(n))
        # print(f'Currently at {len(included_primes)} included primes')
        if len(included_primes) == 100:
            break
    n.add(find_next(n))

print(sum(included_primes))
