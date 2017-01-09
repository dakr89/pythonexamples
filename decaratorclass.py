
# import pdb
class decoratorclass(object):
	"""docstring for ClassName"""
	def __init__(self, func,*args):
		self.func = func

		


	def __call__(self,*args):
		print('from hello')
		# pdb.set_trace()
		
		return "<p> {}  </p>".format(self.func(*args))

		
@decoratorclass
def calldecorator(x,y):
	return 'hello from calldec func {0} and {1}'.format(x,y)



print(calldecorator(5,2))