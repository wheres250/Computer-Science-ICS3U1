"""
author: Kvin2K
03/09/2022
password validation
"""
    #Check if the password is valid.

    # This function checks the following conditions
    # if its length is greater than 8 and less than 32
    # if it has at least one uppercase letter
    # if it has at least one lowercase letter
    # if it has at least one numeral
    # if it has any of the required special symbols

import re

while True:
  user_input = input("Enter a password : ")
    # This function checks the following conditions
  is_valid = False
    # if its length is greater than 8 and less than 32
  if (len(user_input)<8 or len(user_input)>32):
    print("Total characters should be between 8 and 32")
    continue
    # if it has at least one uppercase letter
  elif not re.search("[A-Z]",user_input):
    print("It should contain one uppercase letter")
    continue
    # if it has at least one lowercase letter
  elif not re.search("[a-z]",user_input):
    print("It should contain one lowercase letter")
    continue
    # if it has at least one numeral
  elif not re.search("[1-9]",user_input):
    print("It should contain one number")
    continue
    # if it has any of the required special symbols
  elif not re.search("[~!@#$%^&*]",user_input):
    print("It should contain at least one special character ~!@#$%^&*")
    continue
  else:
    is_valid = True
    break

if(is_valid):
  print("Password is valid, Creating account now.")
""" https://www.codevscolor.com/python-check-validity-password """