"""
Author: Kvin, Nguyen
Date: 04/06/2022
the spiderman meme where he points at another spiderman and spiderman points at another spiderman
aka python versus python
aka number guessing game
"""
#importing
import random
#input for user to input a number
user_input1=int(input("Enter number between 1 and 100: "))
tries=1
compguess=random.randint(1, 100)

#logarithms
while compguess != user_input1:
  #if the user guess is too low
    if compguess > user_input1:
        """
        Explanation: trying to find user number
        Args:
        randint (int): 1-100
        compguess (str): computer's guess
        Return:
            if the answer is too low
        """
        print("too low")
        compguess=random.randint(1, 100)
        print(compguess)
  #if the user guess is too high
    elif compguess < user_input1:
        """
        Explanation: trying to find user number
        Args:
        randint (int): 1-100
        compguess (str): computer's guess
        Return:
            if the answer is too high
        """
        print("too high")
        compguess=random.randint(1, 100)
        print(compguess)

        tries += 1
        """
        Explanation: trying to find user number
        Args:
        randint (int): 1-100
        compguess (str): computer's guess
        Return:
            if the answer is correct
        """
  #if the user gets the right answer
print("you got the correct number",user_input1,\
      "and it only took you",tries,"attempt(s)")
