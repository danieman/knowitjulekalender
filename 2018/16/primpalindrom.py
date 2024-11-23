def is_palindrome(arr):
    return arr == arr[::-1]

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i, w, s = 5, 2, n**0.5
    while i <= s:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

digits = [int(d) for d in open('input.txt').read().split(',')]
known_primes = set()

pal_start_idx = []
max_prime_pal = 0
pal_length = 5

for i in range(len(digits)-pal_length+1):
    arr = digits[i:i+pal_length]
    if arr[pal_length//2]%2 and is_palindrome(arr):
        pal_start_idx.append((i, sum(arr)))

for idx, val in pal_start_idx:
    length = pal_length + 2
    while True:
        try:
            idx -= 1
            start, end = digits[idx], digits[idx+length-1]
            if start == end:
                val += 2*start
                if val in known_primes or is_prime(val):
                    known_primes.add(val)
                    if (val > max_prime_pal):
                        max_prime_pal = val
            else:
                break
            length += 2
        except:
            break

print(max_prime_pal)