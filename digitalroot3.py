"""
Author: Kvin2K
Date: 03/30/2022
Digital root
"""
# The digital root of a number is the number that you get when you add together all of the digits of a number, and keep going until the number of digits left is 1. 
# A number is divisible by 3 if the digital root is either 3, 6, or 9.
# Your job is to write a program called digitalroot3.py that allows the user to input a number (I would suggest leaving it as a string). The program will output "Divisible" if the inputted number is indeed divisible by 3, and will print "Not Divisible" otherwise. 

#IPO
import math
 
#Input
#Requests the user to input a number
n = input("please enter number: ")
#Processing
#Using LGI to seperate the numbers
lgi = [int(n)for n in n]
print(lgi)
#Add numbers
def digital_root(n):
  while True:
    n_list = [int(d) for d in str(n)]
    if len(n_list) == 1:
      return n
    n = sum(n_list)
print(digital_root)