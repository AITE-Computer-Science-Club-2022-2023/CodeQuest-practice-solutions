import sys

num_cases = int(sys.stdin.readline())

for case in range(num_cases):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    sum = n1 + n2
    product = n1 * n2
    print(f'{sum} {product}')