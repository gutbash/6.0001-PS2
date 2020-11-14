# Problem Set 2, hangman.py
# Name: Sebastian
# Collaborators: -
# Time spent: November 12-14, 2020

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
  """
  Returns a list of valid words. Words are strings of lowercase letters.
  
  Depending on the size of the word list, this function may
  take a while to finish.
  """
  print("Loading word list from file...")
  # inFile: file
  inFile = open(WORDLIST_FILENAME, 'r')
  # line: string
  line = inFile.readline()
  # wordlist: list of strings
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist



def choose_word(wordlist):
  """
  wordlist (list): list of words (strings)
  
  Returns a word from wordlist at random
  """
  return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  for i in secret_word:
    if i in letters_guessed:
      continue
    else:
      return False
  return True

# print(is_word_guessed('app', ['a', 's']))

def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''
  word = ''

  for i in secret_word:
    if i in letters_guessed:
      word += i
    else:
      word += '_ '
  return word

def get_available_letters(letters_guessed):
  '''
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
  '''
  remaining = ''

  for i in list(string.ascii_lowercase):
    if i in letters_guessed:
      continue
    else:
      remaining += i
  return remaining

def hangman(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses

  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
  
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
  
  Follows the other limitations detailed in the problem write-up.
  '''
  print('Welcome to the game Hangman.')
  print(secret_word)

  guess = 6
  guessed = []
  warning = 0

  while guess != 0:

    print('------------------------------------')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {guess} guesses left.')
    print('Available letters: ' + get_available_letters(guessed))

    letter = (input('What letter will you guess?: ')).lower()

    if not letter in string.ascii_lowercase:
      warning += 1
      print(f'Invalid guess. Warnings: {warning}')
      if warning == 3:
        warning = 0
        guess -= 1
        print('Guess lost.')
        continue
      continue

    if letter in guessed:
      print('That letter has already been guessed.')
      warning += 1
      if warning == 3:
        warning = 0
        guess -= 1
        print('Guess lost.')
        continue
      continue

    guessed.append(letter)
    print(get_guessed_word(secret_word, guessed))

    if letter in secret_word:
      print('Correct')
    else:
      print('Incorrect')
      guess -= 1
      if letter in 'aeiou':
        guess -= 1
    
    if is_word_guessed(secret_word, guessed) == True:
      print('------------------')
      print('Congratulations, you won.')
      print(f'Score: {guess * len(guessed)}')
      return
    else:
      print('Keep guessing!')
      
  print('------------------')
  print('Sorry, you lost.')
  print(f'The word was {secret_word}')
  return
  
# print(hangman(choose_word(wordlist)))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  '''
  my_word: string with _ characters, current guess of secret word
  other_word: string, regular English word
  returns: boolean, True if all the actual letters of my_word match the 
      corresponding letters of other_word, or the letter is the special symbol
      _ , and my_word and other_word are of the same length;
      False otherwise: 
  '''
  my_word = my_word.strip(' ')
  my_word = my_word.split(' ')
  my_word = ''.join(my_word)

  if len(my_word) != len(other_word):
    return False

  idx = 0
  checked = []
  for l in my_word:
    if l == '_':
      checked.append(other_word[idx])
      idx += 1
      continue
    elif my_word[idx] == other_word[idx]:
      if other_word[idx] in checked:
        return False
      idx += 1
      continue
    else:
      return False
  return True

# blah = input()
# word = input()
# print(match_with_gaps('a_ ple', word))

def show_possible_matches(my_word):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

  '''
  lst = ''
  for i in wordlist:
    if match_with_gaps(my_word, i) == True:
      lst += i + ' '
    else:
      continue
  if not lst:
    return None
  return lst

def hangman_with_hints(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses
  
  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
    
  * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word. 
  
  Follows the other limitations detailed in the problem write-up.
  '''

  print('Welcome to the game Hangman with Hints.')
  print(secret_word)
  
  guess = 6
  guessed = []
  warning = 0

  while guess != 0:

    print('------------------------------------')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {guess} guesses left.')
    print('Available letters: ' + get_available_letters(guessed))

    letter = (input('What letter will you guess?: ')).lower()

    if letter == '*':
      guess_match = get_guessed_word(secret_word, guessed)
      print(show_possible_matches(guess_match))
      continue

    if not letter in string.ascii_lowercase:
      warning += 1
      print(f'Invalid guess. Warnings: {warning}')
      if warning == 3:
        warning = 0
        guess -= 1
        print('Guess lost.')
        continue
      continue

    if letter in guessed:
      print('That letter has already been guessed.')
      warning += 1
      if warning == 3:
        warning = 0
        guess -= 1
        print('Guess lost.')
        continue
      continue

    guessed.append(letter)
    print(get_guessed_word(secret_word, guessed))

    if letter in secret_word:
      print('Correct')
    else:
      print('Incorrect')
      guess -= 1
      if letter in 'aeiou':
        guess -= 1
    
    if is_word_guessed(secret_word, guessed) == True:
      print('------------------')
      print('Congratulations, you won.')
      print(f'Score: {guess * len(guessed)}')
      return
    else:
      print('Keep guessing!')
      
  print('------------------')
  print('Sorry, you lost.')
  print(f'The word was {secret_word}')
  return

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
