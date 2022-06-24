"""
Author: Kvin2K
Date: 04/04/2022
making the second letter uppercase
"""
#IPO
#Today we are allowing the user to input a couple words, and we will capitalize some parts!
#here, we are asking the user to enter anything of thier interest.
#Input
txt = input("Type something to test this out: ")
# here, we have decided to split the string to simplify using the enumerations!
#Processing
x = txt.split()
#Now, we capitalize using the upper function!
x = "".join([x.upper() if i % 2 != 0 else x for i, x in enumerate(x)])
#Output
#Printing the modified code!
print(x)