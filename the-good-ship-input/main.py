import sys

#num cases
cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    #num all systems & working systems
    x, y = map(int, sys.stdin.readline().rstrip().split())
    
    #gets all systems
    all_systems = [sys.stdin.readline().rstrip() for system in range(x)]
    
    #removes functional systems
    for system in range(y):
        all_systems.remove(sys.stdin.readline().rstrip())
    
    #returns nonfunctional systems
    for system in all_systems:
        print(system)