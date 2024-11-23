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

def is_juletall(n):
    global primes
    factors = 0
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            factors += 1
            if factors > 9:
                return False
            n //= primes[i]
        else:
            i += 1
            if i >= len(primes):
                return False
    return True if factors == 9 else False

primes = gen_primes(2**9)

# Funnet 14 juletall manuelt for opp til og med 14 toer-faktorer:
juletall = 14

for i in range(2**9, 2**17):
    if is_juletall(i):
        juletall += 1

print(juletall)
# Svar: 914
