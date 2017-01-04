# import os
# import sys
# from test1 import kill

# # sys.path.append(os.path.abspath('D:/notebook'))
# # import hello

# kill.anil()

# # hello.tt.hee()



class Employee:
	location = "hyd"
	d_no = 0
	def __init__(self,name,job):
		self.name = name
		self.job= job
		self.email = name +'.'+job
		Employee.d_no += 1
	@property
	def firstname(self):
		return self.name+'@'+self.job
	 # reglar method will take instatacnce as attribute 
	@property
	def loca(self):
		return self.name+'.'+self.job+'@'+self.location
	@classmethod
	def set_location(cls,locc):
		cls.location = locc
	@classmethod
	def par_str(cls,text):
		name,job = text.split('_')
		return cls(name,job)



# e1 = Employee('anil','google')

# print(e1.firstname)
# print(e1.loca)
d1_st = 'anil_hcl'
# d12_st = 'kumar_boa'
# # name,job = d1_st.split('_')

d2 = Employee.par_str(d1_st)
# # d2 = Employee('kumar','BOA')
# Employee.set_location('delhi')

# print (Employee.location)
# print (d2.loca())
# print (d1.loca())

# # d2 = Employee()
print (d2.firstname)
# print (Employee.firstname(d1))

# class  developer(Employee):
# 	location = "USA"
# 	def __init__(self,name,job,lang):
# 		super().__init__(name,job)
# 		# Employee.__init__(slef,name,job)
# 		self.lang = lang
# 	def loca(self,expe):

# 		self.expe = expe
# 		return 	self.expe+'anilll guess what'+super().location




# dev1 = developer('reddy','TCS','python')

# dev2 = developer('dappili','wipro','java')
# # print(dev1.loca('uk'))

