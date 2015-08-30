def updateHand(hand,word):

	newHand = hand.copy()
	for letter in word:
		newHand[letter] -= 1
		if newHand[letter] == 0:
			del(newHand[letter])		


	print newHand

updateHand({'g':1,'d':2,'o':6},'dogd')
