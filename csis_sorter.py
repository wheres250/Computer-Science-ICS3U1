"""
Author: Kvin2K
03/08/2022
Lab 2
"""
#Input
#The input will consist of four positive floating point numbers. 
#1
a = float(input('First number: '))
#2
b = float(input('Second number: '))
#3
c = float(input('Third number: '))
#4
d = float(input('Fourth number: '))

#Processing
#now that the user has inputted their 4 numbers of choice, we will find the largest number.

#if the largest number was a
if a > b and a > c and a > d: 
    biggest_num = a

#if the largest number was b
if b > a and b > c and b > d:
    biggest_num = b

#if the largest number was c
if c > a and c > b and c > d:
    biggest_num = c

#if the largest number was d
if d > a and d > b and d > c:
    biggest_num = d

# now we find the second biggest number

# if second biggest was a
if a > b and a < c and a > d or a < b and a > c and a > d or a > b and a > c and a < d:
    second_biggest = a
# if second biggest was b

if b > a and b < c and b > d or b < a and b > c and b > d or b > a and b > c and b < d:
    second_biggest = b
# if second biggest was c

if c > a and c < b and c > d or c < a and c > b and c > d or c > a and c > b and c < d:
    second_biggest = c
# if second biggest was d

if d > a and d < c and d > b or d < a and d > c and d > b or d > a and d > c and c < d:
    second_biggest = d

# now we find the third biggest number

#if third biggest number was a
if a < b and a > c and a < d or a > b and a < c and a < d or a < b and a < c and a > d:
    third_biggest = a

#if third biggest number was b
if b < a and b > c and b < d or b > a and b < c and b < d or b < a and b < c and b > d:
    third_biggest = b

#if third biggest number was c
if c < a and c > b and c < d or c > a and c < b and c < d or c < a and c < b and c > d:
    third_biggest = c

#if third biggest number was  d
if d < a and d > c and d < b or d > a and d < c and d < b or d < a and d < c and c > d:
    third_biggest = d

# now we find the smallest number
# if the smallest number was a
if a < b and a < c and a < d:
    smallest_num = a

# if the smallest number was b
if b < a and b < c and b < d:
    smallest_num = b

# if the smallest number was c
if c < a and c < b and c < d:
    smallest_num = c

# if the smallest number was d
if d < a and d < b and d < c:
    smallest_num = d

# output lol pray for me
print(biggest_num, second_biggest, third_biggest, smallest_num)