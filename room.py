import random

# generate codes:
codelength = 2
difficulty = 5
difficulty = (1 / difficulty) * 26 ** codelength
codes = []
rooms = []
letters = "abcdefghijklmnopqrstuvwxyz"
while len(codes) <= difficulty:
    newcode = ""
    while len(newcode) < codelength:
        newcode += random.choice(letters)
    codes.append(newcode)
    codes = list(set(codes))

print(codes)


class roomclass:
    def __init__(self):
        self.code = random.choice(codes)


for code in codes:
    rooms.append(roomclass())
