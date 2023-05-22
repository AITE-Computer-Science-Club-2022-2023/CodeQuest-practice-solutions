import sys

cases = int(sys.stdin.readline().rstrip())

def pythagorean(a, b):
    c = (float(a)**2 + float(b)**2)**0.5
    return c

for case in range(cases):
    a = int(sys.stdin.readline().rstrip())
    coords = {}
    for asteroid in range(a):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        coords[pythagorean(x, y)] = [x, y]
    vals = sorted(coords.keys())
    coords = {key:coords[key] for key in vals}
    for coord in coords:
        x, y = coords[coord]
        print(x, y)