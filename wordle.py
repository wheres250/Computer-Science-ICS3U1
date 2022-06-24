"""
author: Kvin2K
date: 02/08/2022
creation: a wordle clone in text
"""

import random

def file_to_list(file_name, line_list):
    """ Reads a file and puts each line in a list
    
    args:
        file_name - The name of the file
        line_list - The list to be extended
    
    returns:
        list - The list containing the contents of the file
    """
    with open(file_name) as word_file:
        line_list.extend(word_file.read().splitlines())
    return line_list


def is_valid(user_guess, word_list):
    """ Checks to see if a user's guess is a valid guess
    
    args:
        user_guess - The guess the user gave
        word_list - A list of all posiible words
    
    returns:
        bool - Whether or not the word is a valid wordle word
    """
    ## Check if the word is valid
    if len(user_guess) != 5:
        print("That word was invalid: Must be 5 letters")
        return False

    ## Check to see if user_guess is in our wordlist!
    if user_guess not in word_list:
        print("That word was invalid")
        return False
    
    return True


def check_word(user_guess, random_word):
    """ Checks word against random word and gives hints as necessary
    
    args:
        user_guess - The guess the user gave
        random_word - The word to be guessed by the user
    
    returns:
        bool - Whether or not the user correctly guessed the word
    """
    ## Check if the user's word equals the random word
    if user_guess == random_word:
        ## if above is true then the game is over
        print("Congratz! You got it")
        return True
        
    ## otherwise figure out letter positions
    # Print two spaces to line up our hint with the user's prev guess
    print("  ", end="")
    # Go through every letter in the user's guess
    for pos, letter in enumerate(user_guess):
        # If that letter is in the random word
        if letter in random_word:
            ## if that letter is in the right position -> print the letter
            if letter == random_word[pos]:
                # end="" makes sure that no new line happens after the print
                print(letter, end="")
            ## otherwise the letter is in the wrong position -> print ~
            else:
                print("~", end="")
        # Otherwise if the letter was not in the word -> print _
        else:
            print("_", end="")
    # Finally moves us onto the next line
    print()
    return False

def main():
    """ The main entry point of our Wordle game. """
    word_list = file_to_list("wordle_wordlist.txt", [])
    random_word = random.choice(word_list)
    word_list = file_to_list("all_words.txt", word_list.copy())

    print(len(word_list))

    # Loop 6 times
    for tries_left in range(6, 0, -1):
        print("BTW you have", tries_left, "tries left")
        ## Allow user to enter a 5 letter word
        user_guess = input("Enter a 5 letter word\n> ")
        
        ## Check if the word is valid
        while not is_valid(user_guess, word_list):
            user_guess = input("Enter a 5 letter word\n> ")
        
        if check_word(user_guess, random_word):
            exit(0)
    
    # You Lose
    print("Awe man! The word was", random_word)


if __name__ == '__main__':
    main()