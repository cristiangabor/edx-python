def maxofThree(a,b,c):

	if a > b:
		bigger=a

	else:
		bigger=b

	if c> bigger:
		bigger=c
	
	print bigger

maxofThree(0,0,0),maxofThree(-3,-10,-1),maxofThree(10,30,100),maxofThree(0,-9,11),maxofThree(-10,0,30)
