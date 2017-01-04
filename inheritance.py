class first:
	sal = 90000
	def __init__(self,name,location):
		self.name = name
		self.location = location
	def details(self):
		return self.name+'@@'+self.location+'-----'+self.lang

class third:

	def __init__(self,age,wil):
		self.age = age
		self.wil = wil
	def details(self):
		return self.age+'@     @'+self.wil



class second(first,third):
	sal = 75000
	def __init__(self,name,location,age,wil,lang):
		super().__init__(name,location)
		super().__init__(age,wil)

		self.lang = lang
	
	def details(self):
		print(super().sal)
		return self.lang


# fir = first('anil','hyd')
sec = second('anil','hyd','28','holidays','python')
print(sec.details())
