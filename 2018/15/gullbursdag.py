birthyears = [int(line.split()[-1][2:]) for line in open('input.txt')]

total = 0
for birthyear in birthyears:
    year = birthyear
    age = 0
    while age ** 2 <= year:
        if age ** 2 == year:
            total += 1
        year += 1
        age = year - birthyear

print(total)