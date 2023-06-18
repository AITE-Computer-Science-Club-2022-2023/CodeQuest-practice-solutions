import sys
import re

d = {'A': 10, 'B': 20, 'C': 30}
class Ship(object):
    def __init__(self, values):
        self.shipname = values[0]
        self.shipclass = d[values[1]]
        self.xcor = int(values[2])
        self.ycor = int(values[3])
    def __repr__(self):
        return f'Destroyed Ship: {self.shipname} xLoc: {self.xcor}'
    def __lt__(self, k):
        if self.xcor == k.xcor:
            return self.ycor < k.ycor
        else:
            return self.xcor > k.xcor

pattern = re.compile(r'^(\w+)_([A-C]):(\d+),(\d+)$')
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    ships = []
    for subcaseNum in range(int(sys.stdin.readline().rstrip())):
        ships.append(Ship(re.search(pattern, sys.stdin.readline().rstrip()).groups()))
    for i in range(len(ships)):
        ships.sort()
        print(ships.pop())
        for ship in ships:
            ship.xcor -= ship.shipclass
