import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

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



# matplotlib.style.use('ggplot')
# ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# ts = ts.cumsum()
# plt.figure()
# ts.plot()
# plt.show()


# class dummy:
# 	# def _prt(self):
# 	# 	print('fromm  prr'+self.__name)
# 	# _name = 'anil'
	
# 	def __init__(self):
# 		# self.__name = name
# 		print('from init')
# 	def hello(self):
# 		# self.__name = name
# 		print('from self')
# 	@classmethod
# 	def clmethod(cls):
# 		print('heloo from cl')
# 	@staticmethod
# 	def stmethod():
# 		print('heloo from cst')
# 	def sample():
# 		print('hello')

# # d  = dummy()
# # d._dummy__name
# # print(d._name)
# # dummy.hello()
# # dummy.clmethod()
# # print(type(dummy.sample))
# # dummy.hello()
# dummy.clmethod()
# dummy.stmethod()
# dummy.sample()

from collections import OrderedDict

# table = OrderedDict((
#     ("Item", ['Item0', 'Item0', 'Item0', 'Item1']),
#     ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
#     ('USD',  ['1', '2', '3', '4']),
#     ('EU',   ['1€', '2€', '3€', '4€'])
# ))


# data = pd.DataFrame(table)
# print(data.stack())

# pi = data.pivot_table(index='Item',columns='CType',values='USD',aggfunc='sum')
# row_idx_arr = list(zip(['r0', 'r0'], ['r-00', 'r-01']))
# print(list(["string","hellos"],))

# index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),('two', 'a'), ('two', 'b')])
# s = pd.Series(range(1,5),index=index)
# data = pd.DataFrame(s)
# print(data.T)

# ind = pd.MultiIndex.from_tuples([('gender','M'),('gender','F'),('age','young'),('age','durty')])
# data1 = pd.DataFrame(pd.Series(range(5,9),index=ind))
# print(data1.unstack(level=0,fill_value=0))


# df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
# cls = [('one','c'),('one','d')]
# df.columns = pd.MultiIndex.from_tuples(cls)
print(" hellooo ".strip())
