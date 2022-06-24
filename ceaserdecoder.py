"""
author: Kvin2K
date 02/23/2022 tuesday
decrypt a message using the ceasar cipher
"""

# Input
# (msg to encrypt[any])
message = input(' enter a message to be decrypted! ').lower()
shift = int(input ('enter a shift amount: '))
# Processing
decrypted_message = ' '
for char in message: 
    # Convert the letter to a number
    char_num = ord (char) 
    # then subtract a shift to the number
    char_num = char_num - shift
    if char_num < ord('a'):
        overflow = char_num - ord('z') + 1
        char_num = ord('a') + overflow
    # Convert the shifted number back to a character
    # and add it to out decrypted message
    decrypted_message = decrypted_message + chr(char_num)
   
# Output
# (an decrypt msg [any])
print(decrypted_message)