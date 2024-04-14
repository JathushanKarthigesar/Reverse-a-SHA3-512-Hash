## I need to import a word-list (Common words out there)

## Then I will calculate SHA3-512 hash of those words

# I will compare it with the given Hash

# If I found a result, I will look at the word-list

import hashlib

given_Hash = "a2099f4c2c2de141afb474dfe4b765ce83448100e77f4359314d94807b00862d53316c03963fc60cbdbd7bc6915778f1830f0f4fd9364a4bc71a09c5e83a0a67"


with open('pass.txt') as myFile:

    word_list = myFile.readlines()

    for items in word_list:
       
       words = items.strip()

       hashed_words = hashlib.sha3_512(words.encode()).hexdigest()

       if given_Hash == hashed_words:
           print(words)