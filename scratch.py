import string
import random

# print('apple' == 'apple')
# print('z' in 'apple')

# for i in range(3):
#     print('test')

# def get_available_letters(letters_guessed):
#   '''
#   letters_guessed: list (of letters), which letters have been guessed so far
#   returns: string (of letters), comprised of letters that represents which letters have not
#     yet been guessed.
#   '''
#   remaining = ''

#   for i in list(string.ascii_lowercase):
#     if i in letters_guessed:
#       continue
#     else:
#       remaining += i
#   return remaining

# guessed = ['a']

# print(get_available_letters(guessed))
# print('hello'.lower())

word = 'wo_ rd'

print(word.split(' '))