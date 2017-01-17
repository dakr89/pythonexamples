# import pandas as pd

# print(pd.test)
# @staticmethod


# class anil:
# 	@staticmethod
# 	def hello(x,y):
# 		print(' dssd ot',x+y)


# 	@staticmethod
# 	def subb(x,y):
# 		print ('sub value is ',x-y)



# import json
# # d = {'anil':'name'}
# # data = {'key': 'value', 'whatever': [1, 42, 3.141, 1337]}
# # ff = open('intro.json','w')
# # json.dump(data,ff)
# with  open('intro.json') as e:

# 	kk = json.load(e)
# 	print(kk)

# # with open('intro.json') as json_data:
# #     d = json.load(json_data)
# #     print(d)



# import matplotlib.pyplot as plt
# import matplotlib
# import pandas as pd
# import numpy as np

# matplotlib.style.use('ggplot')
# ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# ts = ts.cumsum()
# plt.figure()
# ts.plot()
# plt.show()

def first():
	print('hello')


class dummy:
	# def _prt(self):
	# 	print('fromm  prr'+self.__name)
	# _name = 'anil'
	
	def __init__(self):
		# self.__name = name
		print('from init')
	def hello(self):
		# self.__name = name
		print('from self')
	@classmethod
	def clmethod(cls):
		print('heloo from cl')
	@staticmethod
	def stmethod():
		print('heloo from cst')
	def sample():
		print('hello')

# d  = dummy()
# d._dummy__name
# print(d._name)
# dummy.hello()
# dummy.clmethod()
# print(type(dummy.sample))
# dummy.hello()
dummy.clmethod()
dummy.stmethod()
dummy.sample()