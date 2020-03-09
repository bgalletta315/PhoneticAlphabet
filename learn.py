# Creates random string of 3 letters and 5 numbers
# to help learn the Phonetic Alphabet

import random
from dictionaries import Phonetic_Alphabet, Numbers, Letters

def conv_phonetic(list):
    converted = []
    for key in list:
        if key in Phonetic_Alphabet:
            converted.append(str(Phonetic_Alphabet[key]))
        else:
            converted.append(str(key))
    return converted

while True:
    # Choose random numbers and letters
    rand_letters = []
    rand_nums = []
    for x in range(3):
        rand_letters.append(random.choice(Letters).upper())
    for y in range(5):
        rand_nums.append(random.choice(Numbers))

    # Put into one string and shuffle
    rand_list = rand_letters + rand_nums
    random.shuffle(rand_list)
    converted_list = conv_phonetic(rand_list)
    rand_string = "".join(rand_list)

    # Displays
    print('Random String:', rand_string)
    input('Press ENTER to see the Phonetic conversion')
    print('Phonetic Conversion:')
    print(converted_list)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Repeat?
    userIn = input('Try again? [y/n]: ')
    if userIn != 'y':
        break
    else:
        print('Restarting...\n.\n.\n')
