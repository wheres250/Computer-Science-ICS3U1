"""
author: Kvin2K
date 02/22/2022 tuesday
Encrypt a message using the ceasar cipher
"""

# Input
# (msg to encrypt[any])
message = input(' enter a message to be encrypted! ').lower()
shift = int(input ('enter a shift amount: '))
# Processing
# a b c d e f ... w x y z (z + 2? = b)
# 1 2 3 4 5 6 ... (1 + 2 = 3)
encrypted_message = ' '
for char in message: 
    # Convert the letter to a number
    char_num = ord (char) 
    # then add a shift to the number
    char_num = char_num + shift
    if char_num > ord('z'):
        overflow = char_num - ord('z') - 1
        char_num = ord('a') + overflow
    # Convert the shifted number back to a character
    # and add it to out encrypted message
    encrypted_message = encrypted_message + chr(char_num)
   
# Output
# (an encrypt msg [any])
print(encrypted_message)