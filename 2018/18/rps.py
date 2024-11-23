def winner(s):
    if s in ['SPP', 'PRR', 'RSS']:
        return 'a'
    elif s in ['PSP', 'RPR', 'SRS']:
        return 'b'
    elif s in ['PPS', 'RRP', 'SSR']:
        return 'c'
    elif len(set(s)) in [1,3]:
        return None
    else:
        return 'draw'

def draw(s, first, second):
    if s in ['SP', 'PR', 'RS']:
        return first
    elif s in ['PS', 'RP', 'SR']:
        return second
    else:
        return 'draw'

def whodrew(s):
    if s in ['SSP', 'PPR', 'RRS']:
        return 'a', 'b'
    elif s in ['SPS', 'PRP', 'RSR']:
        return 'a', 'c'
    elif s in ['PSS', 'RPP', 'SRR']:
        return 'b', 'c'


points = {'a': 0, 'b': 0, 'c': 0}
input = open('input.txt').read().strip()

i = 0
while True:
    try:
        game = input[i:i+3]
        i += 3
        if winner(game) == 'draw':
            f, s = whodrew(game)
            while True:
                game = input[i:i+2]
                i += 2
                if draw(game, f, s) == 'draw':
                    continue
                else:
                    points[draw(game, f, s)] += 1
                    break
        elif not winner(game):
            continue
        else:
            points[winner(game)] += 1
    except:
        break

print(','.join([str(x) for x in points.values()]))