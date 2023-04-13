import sys

def is_anagram(word1, word2):
    if word1 != word2:
        for char in word1:
            if word1.count(char) != word2.count(char):
                return False
        return True
    else:
        return False

num_cases = int(sys.stdin.readline())
for case in range(num_cases):
    w1, w2 = sys.stdin.readline().rstrip().split('|')
    if is_anagram(w1, w2):
        print(f'{w1}|{w2} = ANAGRAM')
    else:
        print(f'{w1}|{w2} = NOT AN ANAGRAM')
