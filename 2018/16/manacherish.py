from sympy.ntheory.primetest import isprime

digits = [int(d) for d in open('input.txt').read().split(',')]
known_primes = set()
max_pal_sum = 0
for i, val in enumerate(digits):
    if val % 2:
        l = r = i
        try:
            while digits[l-1] == digits[r+1]:
                val += 2*digits[l-1]
                if val in known_primes or isprime(val):
                    known_primes.add(val)
                    if val > max_pal_sum:
                        max_pal_sum = val
                l, r = l-1, r+1
        except:
            continue

print(max_pal_sum)