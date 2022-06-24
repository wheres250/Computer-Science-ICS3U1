"""
Author: Kvin2K
Date: 03/22/2022
Description: Practice with primes
"""
import sys
import math
#Check if a number is prime
user_number = input("Please enter a number: ")
while not user_number.isnumeric():
    user_number = input("Please enter only numbers: ")

#Safe cast to an integer
user_number = int(user_number)

is_prime = True
for f in range(2, user_number):
    if user_number % f == 0:
        is_prime =  False
        break

print(user_number, "is prime?",  is_prime)

#Generate prime numbers the bad way
try: 
    prime_cap = int(input("Enter the maximum number to generate primes: "))
except ValueError:
    print("input must be a number", file=sys.stderr)
    exit(1)

prime_list = []
for number in range(2, prime_cap+1):
    is_number_prime = True
    for f in range(2, int(math.sqrt(number))+1):
        if number % f == 0:
            is_number_prime = False
            break

    if is_number_prime:
        prime_list.append(number)


print(prime_list)

#Generate prime numbers the good way (eratosthenes)
try: 
    prime_cap = int(input("Enter the maximum number to generate primes: "))
except ValueError:
    print("input must be a number", file=sys.stderr)
    exit(1)

prime_list = []
for number in range(2, prime_cap+1):
    is_number_prime = True
    for p in prime_list: 
        if number % p == 0:
            is_number_prime = False
            break
        if p > int(math.sqrt(number)):
            break

    if is_number_prime:
        prime_list.append(number)


print(prime_list)