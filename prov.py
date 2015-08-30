import string
lettersGuessed=['e','i','k','p','a','l']
letters=[]
letters=string.ascii_lowercase
lettersbackup=''
rightletters=''

for e in letters:
	if e in lettersGuessed:
		lettersbackup +=e
	else:
		rightletters +=e
print letters
print rightletters
