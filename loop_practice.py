"""
Author: Kvin2K
Date: 03/25/2022
Description: Loop practices (9 questions)
"""
import random
#IPO
#Question 1
#Write a for loop that prints all the numbers from 0 up to, but not including 100.
while True:
    var = int(input("Enter the question you would like to answer: "))
    if var == 1:
        for number in range(100):
            print(number)

        #Question 2
        #Write a for loop that prints all of the odd numbers from 1 up to, but not including 100
    if var == 2:
        for num in range(0, 100 + 1):
            
            # checking condition
            if num % 2 != 0:
                print(num, end = " ")

        #Question 3
        #Write a for loop that adds all of the numbers from 0 up to, but not including 100 (4950)
    if var == 3:
        sum = 0
        for i in range(1, 100):
            sum = i + sum
            print(sum)
        #Question 4
        #Write a for loop that multiplies all of the numbers from 1 up to, but not including 10 (362880)
    if var == 4:
        sum = 1
        for i in range (1,10,1):
            sum = i * sum
            print(sum)

        #Question 5
        #Create a list that contains at least 5 items on a grocery list. Write a for loop that prints each item of that list with a ☐ (you can copy/paste that box).
    if var == 5: 
        list = ["Potato" , "Rice" , "Dressing" , "Chips" , "Apples"]
        for list in list:
            print( list, "☐")

        #Question 6
        #Create a string variable that contains a random sentence. Write a for loop that counts the number of times the letter ‘e’ appears in the sentence.
    if var == 6:
        sum = 0
        sentence = input("enter random sentence: ")
        for z in sentence:
            if z == "e":
                sum = 1 + sum
        print(sum, "e's")

        #Question 7
        #Write a while loop that prints out a random number between 1 and 100 then asks the user to see if they’d like to see another one. If they type ‘yes’, then display another number, if they say ‘no’, then exit the loop.
    if var == 7:
        while True:
            from random import *

            x = randint(1 , 100)
            print(x)

            g = input("Another random number?: ")
            if g == "no":
                break

        #Question 8
        #Write a while loop that asks a user to input their favourite ‘valid’ word. A word is valid if it starts with an uppercase letter. 
    if var == 8:
        word = input("what is your favourite word?: ")
        if not word[0].isupper():
            print("this word is invalid, please try again")
        else: print("word is valid")


        #Question 9
        #Write a while loop that asks the user to enter a floating point number. Print out the floating point number and it’s type once you have confirmed it’s a float.
    if var == 9:
        x = (input("Enter any number that you would like: "))
        if not x.isdigit():
            print("this must be a number")
        else:
            y= float(x)
            print(x, type(y))