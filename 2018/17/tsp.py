from itertools import permutations

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def total_dist(pts):
    return sum([dist(p, pts[i + 1]) for i, p in enumerate(pts[:-1])])

def tsp(pts, start):
    return min([p for p in permutations(pts) if p[0] == start], key=total_dist)

coords = """
7.1,10.5
18.8,9.2
2.1,62.1
74.2,1.5
58.4,5.6
15.9,6.2
44.5,15.6
88.1,53.4
36.2,84.2
26.9,8.5
"""

pts = [(float(u),float(v)) for u,v in [line.split(',') for line in coords.strip().split('\n')]]
print(round(min([total_dist(tsp(pts, pts[p])) for p in range(len(pts))])))
