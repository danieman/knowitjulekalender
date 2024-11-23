instructions = open('input.txt').read().strip()
visited = {(0,0)}
x, y = 0, 0
x_min, x_max, y_min, y_max = 0, 0, 0, 0
i = 0
for i in range(0, len(instructions), 2):
    s, d = int(instructions[i]), instructions[i+1]
    for j in range(s):
        if d == 'H':
            x += 1
            if x > x_max: x_max = x
        elif d == 'F':
            y += 1
            if y > y_max: y_max = y
        elif d == 'V':
            x -= 1
            if x < x_min: x_min = x
        elif d == 'B':
            y -= 1
            if y < y_min: y_min = y
        visited.add((x,y))

total_squares = (x_max - x_min + 1) * (y_max - y_min + 1)

print('{:.16f}'.format(len(visited) / (total_squares-len(visited))))