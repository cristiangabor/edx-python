def gcdIter(a,b):
	test=min(a,b)
	print test % a
	while a%test !=0  or b%test !=0:
		test -=1
	print test
	
gcdIter(9,12)


