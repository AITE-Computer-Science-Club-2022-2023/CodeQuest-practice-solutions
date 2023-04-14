import sys

num_cases = int(sys.stdin.readline())
for case in range(num_cases):
    speed, distance = map(float, sys.stdin.readline().rstrip().split(':'))
    if speed == 0:
        print('SAFE')
    else:
        time = distance / speed
        if time <= 1:
            print('SWERVE')
        elif 1 < time <= 5:
            print('BRAKE')
        else:
            print('SAFE')
