#  this example will explain what is the difference between call and init function

#  init example
# class  init_call:
# 	#  crate init  function in side of it 
# 	def __init__(self,a,b):
# 		self.a = a
# 		self.b = b
# 		print('from init method and the entered values are:  ',self.a,self.b)



# obj_init_call =  init_call(5,6)

#  call  example
# class  init_call:
# 	#  call method will take instance as a parameter (self is te instacne for a class)
# 	def __call__(self):

# 		print('from init method and the entered values are:  ')



# # obj_init_call =  init_call()
# # obj_init_call()
# init_call()()

class call_init(object):
	"""docstring for ClassName"""
	def __init__(self,*args):
		self.a = args[0]
		self.b = args[1]
		print('from init method')


	def __call__(self):
		print("from call function")





ci = call_init(1,2)
ci()


