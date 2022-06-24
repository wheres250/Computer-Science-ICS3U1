"""
Author: Kvin2K
Date: 04/08/2022
Rock Paper Scissors
"""
import random
# Constants
ROCK, PAPER, SCISSORS = range(1, 4)
COMP_WIN, USER_WIN, TIE = range(4, 7)
def get_user_choice():
    """Get user choice
    Returns: 
        (int): integer representring one of rock, paper, and scissors.
    """
    print("Please enter choice")
    print("1: 👊")
    print("2: ✋")
    print("3: ✌")
    user_choice = input()
    if not user_choice.isnumeric():
        print("Try again.")
        return get_user_choice()
    elif int(user_choice)not in( 1 , 2 , 3 ):
        print("Number must be 1 or 2 or 3")
        return get_user_choice()
    else:
        return int(user_choice)

# Computer Choosing Rock
def compare_object(computer_choice, user_choice):
    
    if computer_choice == ROCK and user_choice == PAPER:
        print("User wins")
        return USER_WIN
    elif computer_choice == ROCK and user_choice == SCISSORS:
        print("Computer win")
        return COMP_WIN
    elif computer_choice == ROCK and user_choice == ROCK:
        print("tie")
        return TIE

# Computer Choosing Paper
def compare_object(computer_choice, user_choice):
    
    if computer_choice == PAPER and user_choice == PAPER:
        print("Tie")
        return TIE
    elif computer_choice == PAPER and user_choice == SCISSORS:
        print("User wins")
        return USER_WIN
    elif computer_choice == PAPER and user_choice == ROCK:
        print("Computer wins")
        return COMP_WIN

# Computer Choosing Scissors
def compare_object(computer_choice, user_choice):
    
    if computer_choice == SCISSORS and user_choice == PAPER:
        print("Computer wins")
        return COMP_WIN
    elif computer_choice == SCISSORS and user_choice == SCISSORS:
        print("Tie")
        return TIE
    elif computer_choice == SCISSORS and user_choice == ROCK:
        print("User wins")
        return USER_WIN


def main():
    # Computer generates guess
    computer_choice = random.randint(1, 3)
    # User makes choice
    users_choice = get_user_choice()

    # Player score
    computer_score = 0
    user_score = 0 

    # TODO: Make sure correct
    while computer_score < 2 and user_score < 2:
            # Compare computer vs user
        winner = compare_object(computer_choice, users_choice)
    # Computer generates guess
        computer_choice = random.randint(1, 3)
        # User makes choice
        users_choice = get_user_choice()
    # Winner gets a point
    if winner == COMP_WIN:
        computer_score += 1
    elif winner == USER_WIN:
        user_score += 1

    # BO3
    if computer_score == 2:
        print("The Computer Wins 🎂")
    else: 
        print("The user wins! 👍")

if __name__ == '__main__':
    main()
