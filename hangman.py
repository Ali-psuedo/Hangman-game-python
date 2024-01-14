# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "./ps2/words.txt"

def load_words():
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    secret_word_letters = list(secret_word)
    letters_guessed = list(letters_guessed)
    if secret_word_letters == letters_guessed:
      return True
    else:
      return False

def get_available_letters(secret_word, letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    global return_list
    return_list = []
    for i in secret_word:
        if i in letters_guessed == False:
            return_list.append('_')
    return_argument = ("Your letter", return_list, "is in the word")
    return ''.join(return_list)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = []
    secret_word = list(secret_word)
    for x in secret_word:
      if x in letters_guessed != None: 
        guessed.append(x)
      else:
        guessed.append('_')

    return ''.join(guessed) 
secret_word = choose_word(wordlist)
guess_update = '_' * len(secret_word)

def hangman(secret_word):
    global guess_update
    no_of_guesses = 6
    letter_iter = 0
    i = 0
    input_a = ('Please input the ',letter_iter,'letter: NOTE: You only get one letter per guess, The secret word contains', len(secret_word), 'letters')
    while (i < 7):
        print("You have", no_of_guesses ,"guesses")
        guess_update = guess_update + input(input_a)
        if is_word_guessed(secret_word, guess_update) == True:
          return print("Congrats, you guessed the word")
        if guess_update != str:  
            print("Please Enter a lowercase letter")
        i += 1
        guess_update = list(guess_update)
        letter_iter = letter_iter + 1
        no_of_guesses = no_of_guesses - 1
        guess_update = get_guessed_word(secret_word, guess_update)
        # available_letters = get_available_letters(secret_word, guess_update)
        if guess_update == 0:
          print('Your guess', guess_update,  'is not in the word')
        else:
          print(guess_update) 
          # print(available_letters)
        if i == 6:
          print("This is your last try so guess the word!!!!") 
    print(secret_word)
        



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # while len(secret_word) < 4:
    #   choose_word(wordlist) 
    #   if len(secret_word) <= 4: 
    #     hangman(secret_word)
    # secret_word = choose_word(wordlist)

    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
