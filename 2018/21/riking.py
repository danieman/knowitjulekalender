from math import ceil

def is_abundant(n):
	divisors = 1
	for i in range(2, ceil(n**0.5)):
		if n % i == 0:
			divisors += i
			divisors += n//i
		if i**2 == n:
			divisors += i
	return divisors > n

with open('one-million-primes.txt') as f:
	total = 0
	prev = int(f.readline())
	prime = int(f.readline())
	while prev < 10**7:
		if prime == prev + 2:
			if is_abundant(prev + 1):
				total += (prev + 1)
		prev, prime = prime, int(f.readline())

print(total)