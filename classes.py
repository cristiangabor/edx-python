class intSet(object):
	def __init__(self):
		self.vals=[]


	def insert(self,e):
		if not e in self.vals:
			self.vals.append(e)
	
	def member(self,e):
		return e in self.vals

	def remove(self,e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')

	def __str__(self):
		self.vals.sort()
		return '{' + ','.join([str(e) for e in self.vals]) + '}'

	def intersect(self,i):
		commonValueSet=intSet()
		for val in self.vals:
			if i.member(val):
				commonValueSet.insert(val)
		print commonValueSet
		
s1=intSet()
s1.insert(4)
s1.insert(5)
s1.insert(4)
print s1

s2=intSet()
s2.insert(3)
s2.insert(7)
s2.insert(4)
print s2
s1.intersect(s2)
