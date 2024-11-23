import re

d = {}

for line in open('input.txt'):
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', line.strip()))
    s = (y2-y1)/(x2-x1)
    d[s] = d.get(s, 0) + 1

print(max(d.values()))
