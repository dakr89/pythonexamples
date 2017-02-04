# from test import *
class main(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.hello = "hello"
	def test(self):
		print ("my name is dadasd  {} and age is {} {}".format(self.name,self.age,self.hello))

class sub_main(main):
	def __init(self,name,age):
		super(sub_main,self).__init__()
		
	def test(self):
		super(sub_main,self).test()
		print ("my name is  vvvvv {} and age is {} {}".format(self.name,self.age,self.hello))



s = sub_main('anill',23)
s.test()

# m = main("anil",28)
# m.test()
# s = sub_main("kumar",29)
# s.test()
l = ["anil","kumar","reddy"]
c= 0
# for x,l in enumerate(l):
# 	print(x,l)


l1 = [1,2,3,4]
l2 = [2,3,4,5]

for x,y in zip(l1,l2):
	print (x,y)

# a,b = 4,5
# print (a,b)
# a,b = b,a
# print (a,b)


# di = {"anil":28,
# 		"kumar":29,
# 		"reddy":30}
# # for  key,val in di.items():
# # 	if key == "anil":
# # 		print ("my name is {} and age {}".format(key,val))
# age = di.get('dappili')
# print ("my  age {}".format(age))
# h1 = 'a'
# h2 = ['a','b','c']
# for lett in h2:
# 	if lett== h1:
		# print ('foundd')
def first(msg):
	def second():
		print ('dsdsd',msg)
	return second()
	
first("cc")

# def main(arg):
# 	print ('inside main')
# 	def first():
# 		print ("from first",arg)
# 	def second():
# 		print ('from second',arg)
# 	try:
# 		assert arg == 10
# 		return first
# 	except AssertionError:
# 		return second


# x = main(10)
# y = main(11)
# print (x())
# print (y())






# def  anl():
# 	x = 1
# 	print ('helloodad')
# 	def second():
# 		print ('dasdas',x)
# 		print (second)
# 		return second
# 	second()
# x = anl()


# x = 20
# try:
# 	assert x ==10
# 	print ('xx vaalue is ',x)
# except AssertiobbnError:b
# 	print('getoutt')

