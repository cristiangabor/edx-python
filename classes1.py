import datetime

class Person(object):
	def __init__(self,name):
		'''create a person called name'''
		self.name=name
		self.birthday=None
		self.lastName=name.split(' ')[-1]

	def setBirthday(self,month,day,year):
		'''set self's birthday to birthDate'''
		self.birthday=datetime.date(year,month,day)

	def getAge(self):
		'''returns self's current age in days'''
		if self.birthday== None:
			raise ValueError
		return (datetime.date.today()-self.birthday).days

	def getLastName(self):
		'''return self's last name'''
		return self.lastName

	def __lt__(self,other):
		if self.lastName==other.lastName:
			return self.name< other.name
		return self.lastName<other.lastName



	# other methods

	def __str__(self):
		'''return self's name'''
		return self.name

class MITPerson(Person):

	nextIdNum=0 # next ID number to asign

	def __init__(self,name):
		Person.__init__(self,name) # initialize Person attributes

		# new MITPerson attribute: a unique ID number

		self.idNum=MITPerson.nextIdNum

		MITPerson.nextIdNum +=1

	def getIdNum(self):
		return self.idNum

	# sorting MIT people uses their Id number,not name!

	def __lt__(self,other):
		return self.idNume<other.idNume

class UG(MITPerson):
	def __init__(self,name,classYear):
		MITPerson.__init__(self,name)
		self.year=classYear

	def getClass(self):
		return self.year

class Grad(MITPerson):
	pass

	'''Distinguish Grad from UG'''
def isStudent(obj):
	return isinstance(obj,UG) or isinstance(obj,Grad)


eu=Person("Cristian Florin Gabor")
eu.getLastName()
eu.setBirthday(4,26,1994)
eu.getAge()

eu1=UG('Fred',2015)
eu2=Grad('Angela')

isStudent(eu1)
isStudent(eu2)
eu3=MITPerson('Fred')
isStudent(eu3)
print eu1
