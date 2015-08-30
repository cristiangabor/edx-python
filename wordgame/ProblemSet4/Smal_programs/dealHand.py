
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def dealHand(n):
	
	hand={}

	numVowels = n /3
	for i in range(numVowels):
		x = VOWELS[random.randrange(0,len(VOWELS))]
		hand[x] = hand.get(x, 0) + 1

	for i in range(numVowels, n):    
		x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        



	print hand


dealHand(7)