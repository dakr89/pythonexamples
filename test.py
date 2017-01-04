
# class anil:

# 	# def __init__(self,name):
# 	# 	self.name = 'name'
# 	# 	print('initttt')
# 	# 	def first(self,name):
# 	# 		if self.name == 'anil':
# 	# 			print ('sdfsf')
# 	# 		else:
# 	# 			print ('ddd')
# 	# 	first(self,name)
# 	name = 12
# 	def first(self):
# 		print('hello mr')

# import webbrowser
# import time

# print (time.ctime())

# # for i in range(3):
# # 	time.sleep(5)
# # 	webbrowser.open('www.gmail.com')
# import os
# from os import rename
# import string
# import glob





# for f in glob.glob('*.py'):

# 	if f == 'caller.py':
# 		print(os.path.getsize('caller.py'))
# 		print ('helloo')
# 		c = open(f)

# 		for  k in c:
# 			print (k)			

# 	else:
# 		print (' bye ')


# def main(rid):
# 	x = os.listdir(rid)
# 	res = []
# 	y = os.getcwd()
	
# 	path = os.chdir(r'D:/anil')

	
# 	for i in x:
# 		res.append(rename(i,i.strip("0123456789")))


# 	print(res)

# main(r'D:/anil')

# def foo(bar):
# 	return bar+1


# def test(foo, bar2):
# 	return foo(bar2)


# print (test(foo,5))

# def parent():
# 	print("from parent")
# 	def first():
# 		print("from first")
# 	def second():
# 		print("from second")
# 	def third():
# 		print("from third")


# 	first()
# 	second()
# 	return "helloo"
# print(parent())


# def anil(some_function):

#     def wrapper():
#     	print ('helooo  before the valuueee')
#     	some_function()
#     	print("Something is happening after some_function() is called.")

#     return wrapper

#     return wrapper

# @anil

# def just_some_function():
#     print("Wheee!")

# # just_some_function = anil(just_some_function)

# just_some_function()


name = "anil"
# # lina
# res = ""
# print(len(name)-1)

# for i in range(len(name)-1, -1, -1):
# 	res += name[i]
# print (res)

# import pickle
a = []

# print (a)
# with open('tets.pickle', 'wb') as af:
# 	pickle.dump(a,af)

# with open('tets.pickle', 'rb') as ad:
# 	b = pickle.load(ad)

# print(b)
# def sqr(x): return x ** 2


# print(list(filter(sqr,a)))
# for num in range(2,10):
#     for i in range(2,num):
#         if (num%i==0):
#             break
#     else:
#     	print(num)

# for n in range(2,10):
# 	# print(n)
# 	for i in range(2,n):
# 		# print(i)
# 		if (n%i == 0):
# 			break
# 	else:
# 		print(n)

k = 5
print(k**2)