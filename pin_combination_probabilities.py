import random

# Functions

# Generates a random PIN
def generateRandomPIN(lengthOfPIN):
    randomizedPIN = []
    for i in range(lengthOfPIN):
        randomizedPIN.append(random.randint(0, 9))
    return ''.join(map(str, randomizedPIN))

# Main Program
for i in range(10):
    print(generateRandomPIN(4))
    print()