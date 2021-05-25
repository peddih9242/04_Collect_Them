# list to store each letter from given word
choose_from = []

# take in given word
word = input("word? ")

# append each letter from the word to the list
for item in word:
    choose_from.append(item)

# make another list to have one to choose from and one to remove letters from
letters_needed = choose_from

while choose_from != []:
    chosen = input("Chosen: ") # change to be randomized in base component

    # remove letters from list
    if chosen in choose_from:
        letters_needed.remove(chosen)
        print(choose_from)
    else:
        # show that you got a duplicate
        print("Duplicate!")