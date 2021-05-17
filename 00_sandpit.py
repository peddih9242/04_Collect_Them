import random

# main routine
letters = ["a", "c", "o", "f", "e"]
valid = True
a = 0
c = 0
o = 0
f = 0
e = 0
while not valid:
    chosen = random.choice(letters)
    if chosen == "a":
        a += 1
    elif chosen == "c":
        c += 1
    elif chosen == "o":
        o += 1
    elif chosen == "f":
        f += 1
    else:
        e += 1
    if c == 1 and o == 1 and f == 2 and e == 2:
        print("Coffee!")
