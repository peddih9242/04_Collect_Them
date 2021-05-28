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

# number checker, optionally checks if input
# is between higher and lower boundaries
def num_check(type, question, low=None, high=None):
    valid = False
    while not valid:
        try:
            # ask question
            response = type(input(question))
            # if question does not need a higher and lower 
            # boundary, return response
            if low is None and high is None:
                return response
            else:
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
show_instr = string_check("Have you played this game before (y/n)? ", yes_no, "Please enter yes / no (or y / n)")
if show_instr == "no" or show_instr == "n":
    instructions()

# loop program
keep_going = ""
while keep_going == "":

    # list to store each letter from given word and setup game summary
    choose_from = []

    # take in given word and check that it is not <blank>
    word_valid = False
    while not word_valid:
        word = input("Word: ")
        if word != "":
            word_valid = True
        else:
            print("Please enter a word.")
    price = num_check(float, "Price (or enter 0 for none): ", 0, 20)
    rounds = num_check(int, "How many times do you want to win? ")
    
    # append each letter from the word to the list
    choose_from = list(word)
    game_summary = []

    # make another list to have one to choose from and one to remove letters from
    rounds_played = 0
    tries_total = 0
    while rounds_played != rounds:
      
        rounds_played += 1
        letters_needed = list(word)
        tries = 0
        game_start = False
        while not game_start:
            
            # generate random letter from word
            chosen = random.choice(choose_from)
            tries += 1

            # remove chosen letter from list
            if chosen in letters_needed:
                letters_needed.remove(chosen)
            
            # append to game summary if won
            if letters_needed == []:
                round_statement = "Round {}: Spelt in {} rounds.".format(rounds_played, tries)
                tries_total += tries
                game_summary.append(round_statement)
                game_start = True

    print()
    statement_gen("Game Summary", "!")
    for item in game_summary:
        print(item)
    if price != 0:
        price_total = price * tries_total
        average = price_total / rounds
        print()
        print("The total money spent was ${:.2f}".format(price_total))
        print("The average money spent per win was ${:.2f}.".format(average))
    keep_going = input("Press <enter> to run this program again or any key to quit: ")