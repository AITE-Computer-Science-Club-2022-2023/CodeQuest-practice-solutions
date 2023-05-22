import sys

cases = int(sys.stdin.readline().rstrip())
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

for case in range(cases):

    encryptedMessage = sys.stdin.readline().rstrip()
    shiftValues = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    directionValues = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    decryptedMessage = ''
    shiftIndex = 0
    directionIndex = 0

    for char in encryptedMessage:
        if char not in LETTERS and char.lower() not in LETTERS:
            decryptedMessage += char
        else:
            for letterIndex in range(len(LETTERS)):
                if LETTERS[letterIndex] == char.lower():
                    break

            shiftKey = shiftValues[shiftIndex]
            directionKey = directionValues[directionIndex]

            if directionKey == 0:
                direction = 1 #to the right
            elif directionKey == 1:
                direction = -1 #to the left
            
            charIndex = letterIndex+direction*shiftKey

            if -26 <= charIndex <= 25:
                decryptedMessage += LETTERS[charIndex].lower()
            elif charIndex > 25:
                decryptedMessage += LETTERS[charIndex%25-1].lower()
            elif charIndex < -26:
                decryptedMessage += LETTERS[charIndex%25].lower()
                

            if shiftIndex == len(shiftValues)-1:
                shiftIndex = 0
            else:
                shiftIndex += 1

            if directionIndex == len(directionValues)-1:
                directionIndex = 0
            else:
                directionIndex += 1

    print(decryptedMessage)