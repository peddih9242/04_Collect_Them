import random

a = 0
c = 0
o = 0
f = 0
e = 0
print("Running....")
coffee = False
while not coffee:
    chosen = random.randint(1, 5)
    
    if chosen == 1:
        letter = "a"
        a += 1
    elif chosen == 2:
        letter = "c"
        c += 1
    elif chosen == 3:
        letter = "o"
        o += 1
    elif chosen == 4:
        letter = "f"
        f += 1
    elif chosen == 5:
        letter = "e"
        e += 1

print("You get coffee!")
