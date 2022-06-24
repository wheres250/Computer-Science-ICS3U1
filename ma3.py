"""
Author: Kvin2K
03/04/2022
ceaser cypher encrypter
"""
#1. Does not call .lower() on the input
#2. First, check to see if the character we are looking at isalpha(). If it is, continue with your program as normal, otherwise, simply add the letter to the encrypted string
#3. If you know the character isalpha(), then check to see if the character islower(). If it is, continue as we did, otherwise, copy the code from the lower portion and modify it to work with uppercase too (you just need to change the ord('a') to ord('A') and so on.

#Input
message = input('Enter a message to be encrypted! ')
shift = int(input('Enter a shift amount: '))

#Processing
encrypted_message = ''
for char in message:
    if char.isalpha():
        # check if char is in the alphabet
        if char.islower():
            # if letter is lower keep it to a lowercase letter
            # Convert the letter to a number
            char_num = ord(char)
            # Then add a shift to the number
            char_num = char_num + shift
            if char_num > ord('z'):
                overflow = char_num - ord('z') - 1
                char_num = ord('a') + overflow
            # Convert the shifted number back to a character
            # and add it to our encrypted message
            encrypted_message = encrypted_message + chr(char_num)
            
        elif char.isupper():
            # if the letter is upper keep it to a captial letter
            # Convert the letter to a number
            char_num = ord(char)
            # Then add a shift to the number
            char_num = char_num + shift
            if char_num > ord('Z'):
                overflow = char_num - ord('Z') - 1
                char_num = ord('A') + overflow
            # Convert the shifted number back to a character
            # and add it to our encrypted message
            encrypted_message = encrypted_message + chr(char_num)
    else:
        # if the char is a space or other symbol print out original
        char_num = ord(char)
        encrypted_message = encrypted_message + chr(char_num)

#Output
# (An encrypted message [any string])
print(encrypted_message)
