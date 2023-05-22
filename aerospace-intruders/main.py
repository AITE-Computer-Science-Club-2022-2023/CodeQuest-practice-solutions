import sys
import re 

num_cases = int(sys.stdin.readline().rstrip())
for case in range(num_cases):
    n = int(sys.stdin.readline().rstrip())
    ships = [re.split('[_:,]', sys.stdin.readline().rstrip()) for _ in range(n)]
    for _ in ships:
        min_
