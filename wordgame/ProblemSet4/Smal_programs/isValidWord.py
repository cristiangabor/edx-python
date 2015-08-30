
wordList=['mic','slab','urat','rau']
def isValidWord(word, hand, wordList):
	if word in wordList:
		for i in word:
			if i in hand.keys():
				












isValidWord('rau',{'a':1,'u':2,'i':1,'r':1},wordList)