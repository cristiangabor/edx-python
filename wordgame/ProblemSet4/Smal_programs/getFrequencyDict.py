def getFrequencyDict(sequence,sequence):
	freq={}
	for i in sequence:
		freq[i.lower()]=freq.get(i,0)+1

	print freq


getFrequencyDict('Matador','Matadore')