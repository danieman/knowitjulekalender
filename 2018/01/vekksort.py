total, min = 0, 0
for line in open('input.txt'):
    num = int(line.strip())
    if num >= min: 
        total += num
        min = num

print(total)