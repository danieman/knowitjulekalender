instructions = open('input.txt').read()

x, y = 0, 0
i = 0
while True:
    try:
        s, d = int(instructions[i]), instructions[i+1]
        if d == 'H':
            x += s
        elif d == 'F':
            y += s
        elif d == 'V':
            x -= s
        elif d == 'B':
            y -= s
        else:
            print('Ugyldig retning.')
            break
        i += 2
    except:
        print('End of file (forhåpentligvis)')
        break

print(f'[{x},{y}]')