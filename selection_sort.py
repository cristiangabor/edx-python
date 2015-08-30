L=[2,6,1,5,10,8]
def selSort(L):
	for i in range(len(L)):
		minIndx = i 
		minVal=L[i]
		j=i+1
		while j < len(L):
			if minVal > L[j]:
				minIndx=j
				minVal=L[j]
				
			j +=1

		temp=L[i]
		L[i]=L[minIndx]	
		L[minIndx]=temp
		Total=[]
		Total.append(L[i])
	print Total

selSort(L)

