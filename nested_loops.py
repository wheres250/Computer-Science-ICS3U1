"""
Author: Kvin2K
Date: 03/28/2022
two numbers and print out the multiplication table that starts at 1 and stops at those two numbers
"""
#IPO
#Input
x=int(input('Positive number #1: '))
#asking user for first variable in multiplication table
y=int(input('Positive number #2: '))
#asking user for second variable in multiplication table
j = x + 1
n = y + 1
#Processing
for rows in range(1, j, 1):
    #range of x or j
    end = ''
    #using end here, we clean up the code and allow it to print more neatly.
    for column in range(1, n, 1):
        #range of y or n
        #clean formatting
        end += '{:3} '.format(rows * column)
        #now revisting the "end", we're going to space it out by 3, and use .format to multiply the rows, by the column.
    #Output
    print(end)
    #print final multiplication table.