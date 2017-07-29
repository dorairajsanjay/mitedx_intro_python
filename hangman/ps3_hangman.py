# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''


    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    # fill in the underscores
    _result = ""
    for i in range(len(secretWord)):
        _result = _result + "_"

    # update result to reflect user response
    _resultList = list(_result)
    for letter in lettersGuessed:
        for index in range(len(secretWord)):
            if letter == secretWord[index]:
                _resultList[index] = letter

    # stretch out the return
    result = []
    for letter in _resultList:
        result += letter
        result += " "

    return "".join(result)


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabets = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alphabets:
            alphabets.remove(letter)

    return "".join(alphabets)

def isLetterInSecretWord(secretWord, letterGuessed):
    for i in letterGuessed:
        if letterGuessed not in secretWord:
            return False

    return True


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    #At the start of the game, let the user know how many 
    #  letters the secretWord contains.
    
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    
    max_guesses = 8
    incorrectGuesses = 0

    print("I am thinking of a word that is " + str(len(secretWord)) + " long")
    
    # iterate through the number of guesses
    correct = False
    while(True):
        
        print("-----------")
        
        print("You have " + str(max_guesses - incorrectGuesses) + " guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))

        # Ask the user to supply one guess (i.e. letter) per round.
        guess = input("Please guess a letter:").lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord,lettersGuessed))
            continue

        # The user should receive feedback immediately after each guess 
        # about whether their guess appears in the computers word.
        
        # After each round, you should also display to the user the 
        # partially guessed word so far, as well as letters that the 
        # user has not yet guessed.
        
        # update list of letters guessed
        lettersGuessed.append(guess)
        
        # check if letter is in secret word
        if isLetterInSecretWord(secretWord,guess) == True:
            print("Good guess: " + getGuessedWord(secretWord,lettersGuessed))
        else:
            print("Oops! That letter is not in my word:" + getGuessedWord(secretWord,lettersGuessed))
            incorrectGuesses += 1
            if (incorrectGuesses == 8):
                break
  
        # did the user win
        if isWordGuessed(secretWord,lettersGuessed):
            correct = True
            break
    
    # outside the While loop
    print("-----------")
    if correct == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)