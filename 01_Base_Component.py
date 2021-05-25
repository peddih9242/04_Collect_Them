# next: make an option to skip through to see how many tries
# it takes on average, or play the game and do each choice
# individually

import random

# Functions

# decorate statements
def statement_gen(statement, decoration):
    
    # create decorations
    sides = decoration * 3
    middle = "{} {} {}".format(sides, statement, sides)
    sandwich = decoration * len(middle)
    
    # print statement and decorations
    print(sandwich)
    print(middle)
    print(sandwich)
    return ""

# string checker
def string_check(question, valid_list, error):
    valid = False
    while not valid:
        # ask question
        response = input(question).lower()
        for item in valid_list:
            # check if response is valid
            if response == item[0] or response == item:
                return response
        # if no item is found then print an error
        else:
            print(error)

# number checker
def num_check(question, low, high):
    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))
            # if response is okay, return response
            if low <= response <= high:
                return response
            # print error statements for invalid responses
            else:
                print("Please enter a number between {} and {}.".format(low + 1, high))
        
        except ValueError:
            print("Please enter an integer.")

# print instructions
def instructions():
    statement_gen("INSTRUCTIONS", "*")
    print("Give me a word, I will randomly choose a letter out of the word.")
    print("Once you are able to spell out the word you gave me, you win a free coffee!")
    print("You can set a price to see how much money it will take to win a free coffee.")


# Main Routine

# string check lists
yes_no = ["yes", "no"]

# ask if user has played to decide to print instructions
show_instr = string_check("Have you played this game before (y/n)? ", yes_no, "Please enter yes/no (or y/n)")
if show_instr == "no" or show_instr == "n":
    instructions()

# loop program
keep_going = ""
while keep_going == "":

    # list to store each letter from given word
    choose_from = []

    # take in given word and check that it is not <blank>
    word_valid = False
    while not word_valid:
        word = input("Word: ")
        if word != "":
            word_valid = True
        else:
            print("Please enter a word.")
    price = num_check("Price (or enter 0 for none): ", 0, 20)

    # append each letter from the word to the list
    for item in word:
        choose_from.append(item)

    # make another list to have one to choose from and one to remove letters from
    letters_needed = choose_from
    tries = 0
    while choose_from != []:
        chosen = input("Chosen: ") # change to be randomized in base component
        tries += 1

        # remove letters from list
        if chosen in choose_from:
            letters_needed.remove(chosen)
        else:
            # show that you got a duplicate
            print("Duplicate!")
    statement_gen("Game Summary", "!")
    print("You won, taking {} tries!".format(tries))
    if price != 0:
        price_total = price * tries
        print("The total money spent was ${:.2f}".format(price_total))
    keep_going = input("Press <enter> to keep going or any key to quit: ")