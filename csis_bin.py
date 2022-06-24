"""
author: Kvin Nguyen
02/28/2022
create a python file that converts the binary string into ascii characters and prints out the pig latin string.
"""
# 01100101 01100101 01110100 01101101 01100001 01111001 00100000 01100101 01101101 01100001 01111001 00100000 01110100 01100001 01100001 01111001 00100000 01101000 01100101 01110100 01100001 01111001 00100000 01101111 01110111 01100101 01110010 01110000 01100001 01111001 00100000

#Input
a_binary_string = "01100101 01100101 01110100 01101101 01100001 01111001 00100000 01100101 01101101 01100001 01111001 00100000 01110100 01100001 01100001 01111001 00100000 01101000 01100101 01110100 01100001 01111001 00100000 01101111 01110111 01100101 01110010 01110000 01100001 01111001 00100000"
# Here we give a variable and we name it "a_binary_string."
# it is given the binary code that was sent to me spaced out by 8 characters.

#Processing
binary_values = a_binary_string.split()
#we split the string here.
ascii_string = ""
for binary_value in binary_values:
    an_integer = int(binary_value, 2)

    ascii_character = chr(an_integer)

    ascii_string += ascii_character
# for each binary value in the binary values, we turn it into an int.
#and for ascii_characters, they are now characters, named an_integer.
#finally, the plain ascii string is equal to the ascii characters.

#Output
print(ascii_string)
#outputting "ascii_string" gives us the piglatin format of the binary numbers.

#""" https://www.kite.com/python/answers/how-to-convert-binary-to-string-in-python """
