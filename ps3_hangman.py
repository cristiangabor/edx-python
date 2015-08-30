# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Se incarca cuvintele din fisier..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "cuvintele au fost incarcate."
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
    # FILL IN YOUR CODE HERE...
    count=''

    for i in secretWord:
        if i in lettersGuessed:
            count +=i
        else:
            break
    if count == secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count=''
    for i in secretWord:
        if i in lettersGuessed:
            count +=i
        else:
            count +='_ '
    return count



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters=[]
    letters=string.ascii_lowercase
    lettersright=''
    lettersback=''
    for i in letters:
            if i in lettersGuessed:
                lettersback +=i
            else:
                lettersright +=i
    return lettersright

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
    # FILL IN YOUR CODE HERE...
    lettersGuessed=''
    i=8
    print "Bun venit la Spanzuratoarea!"
    print "Ma gandesc la un cuvant format din",len(secretWord),"litere."
    print "------------------------"

    while i>=1:
        print "Ti-au mai ramas",i,"incercari"
        print "Litere disponibile: ", getAvailableLetters(lettersGuessed)
        input=str(raw_input("Te rog sa introduci o litera: "))
        
        if input in secretWord:
            if input in lettersGuessed:
                print "***********"
                print "Hoopa! Se pare ca aceasta litera ai introdus-o deja", getGuessedWord(secretWord,lettersGuessed) 
            else:
                lettersGuessed += input
                print "###########"
                print "Ai ghicit bine", getGuessedWord(secretWord,lettersGuessed)
                i -=1
        else:
            
            print "!!!!!!!!!!!!!!"
            print "Hoopa! Aceasta litera nu se afla in cuvant: ", getGuessedWord(secretWord,lettersGuessed)
            i -=1

        boola = isWordGuessed(secretWord,lettersGuessed)   
        
        if boola is True:
                print "------------------------"
                print "Felicitari, ai castigat!"
                break

    if boola is False:            
        print "------------------------"            
        print "Imi pare rau ai ramas fara incercari. Cuvantul era: ", secretWord,'.'        
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
