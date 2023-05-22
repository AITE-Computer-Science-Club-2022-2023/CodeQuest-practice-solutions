import sys
cases = int(sys.stdin.readline().rstrip())
letters = "abcdefghijklmnopqrstuvwqyz"
numbers = "0123456789"
for case in range(cases):
    string = sys.stdin.readline().rstrip()
    for char in string:
        if char not in letters and char not in letters.upper() and char not in numbers and char != " ":   
            string = string.replace(char, "")
    print(string)
    