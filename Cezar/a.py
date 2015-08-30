
import string

def buildCoder(cheie):

	# Definirea listelor si a dictionarului

	LISTA_ordonata=[]
	LISTA_codata=[]
	lista_ordonata=[]
	lista_codata=[]
	dict={}

	# Preia Majusculele din ascii si le transfera unei liste

	for i in string.ascii_uppercase:
		LISTA_ordonata.append(i)

	# VARIABILELE
	''' contor1= contor principal, contor2 = contor secundar,
    	CHEIE = cheia necesara codarii mesajului'''

	contor1=0
	contor2=0
	
	# Testarea cheii 

	if cheie >26:
		raise ValueError ('Numarul introdus este prea mare')
	else:
		CHEIE=cheie


	# Realizarea codarii Majusculelor conform cheii date
	for a in range(0,26):
		if CHEIE + contor1 >25:
			LISTA_codata.append(LISTA_ordonata[contor2])
			contor2 +=1
		else:
			LISTA_codata.append(LISTA_ordonata[CHEIE+contor1])
			contor1 +=1

	# Implementarea cheilor si valorilor cu majuscule intr-un dictionar

	for x,y in zip(LISTA_ordonata,LISTA_codata):
		dict[x]= y


	# Preia minusculele din ascii si le transfera unei liste

	for i in string.ascii_lowercase:
		lista_ordonata.append(i)

	# Redefinirea contoarelor 

	contor1=0
	contor2=0
	# Realizarea codarii minusculelor conform cheii date
	for a in range(0,26):
		if CHEIE + contor1 >25:
			lista_codata.append(lista_ordonata[contor2])
			contor2 +=1
		else:
			lista_codata.append(lista_ordonata[CHEIE + contor1])
			contor1 +=1
	# Implementarea tuturor elementelor intr-un dictionar
	for k,l in zip(lista_ordonata,lista_codata):
		dict[k]= l

	print dict
	return dict
# Made from market place got a number of offers from distribuits and suited for '''



