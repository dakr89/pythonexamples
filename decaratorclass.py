

class decoratorclass(object):
	"""docstring for ClassName"""
	def __init__(self, func,*args):
		self.func = func

		


	def __call__(self,*args):
		print('from hello')
		
		return self.func(*args)

		
@decoratorclass
def calldecorator(x,y):
	print('hello from calldec func',x+y)

calldecorator(5,2)