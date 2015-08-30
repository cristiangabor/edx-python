import string
from b import applyShift

def decode():
	# N fr ymj gjxy rfs, 5

	TEXT='Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. Ro rkc loox boqscdobon pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. Sd rkc loox dro dbknsdsyx yp dro bocsnoxdc yp Okcd Mkwzec dy lomywo Tkmu Pvyboi pyb k pog xsqrdc okmr iokb dy onemkdo sxmywsxq cdenoxdc sx dro gkic, wokxc, kxn odrsmc yp rkmusxq.'
	fisier=open('words.txt','r')
	words=fisier.read().split()

	# Variabilele necesare

	cuvinte_gasite=0
	cheie=0
	counter=0

	for i in range(0,26):
		mesaj=applyShift(TEXT,i)
		mesaj_split=mesaj.split(' ')
		for j in mesaj_split:
			if j in words:
				counter +=1
		if counter > cuvinte_gasite:
			cuvinte_gasite=counter
			cheie=i

	print cheie

decode()