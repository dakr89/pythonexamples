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
def fib(n):
	a,b = 0,1
	for i in range(n):
		a,b = b,a+b
	return b
print([fib(i) for  i in range(5)])
# for x in range(0,5):
# 	for j in range(x+1):
# 		print('*', end='')
# 	print('')