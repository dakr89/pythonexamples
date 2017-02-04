# a,b=0,1
# print (a)
# for i in range(10):
# 	c = a+b
# 	a,b= b,c

# 	print (a)

# import os

# def list_dir(path):

# 	sub = os.listdir(path)
# 	for ssub in sub:
# 		kk =  os.path.join(path,ssub)
# 		if os.path.isdir(kk):
# 			list_dir(kk)
# 		else:
# 			print(kk)




# 	# return fullpath
# list_dir('d:/')
# class A(object):
#     def go(self):
#         print("go A go!")
#     def stop(self):
#         print("stop A stop!")
#     def pause(self):
        
#         try:
#         	raise Exception
#         except Exception as e:
#         	print(e)


# a = A()
# a.pause()
# x = [12,3,4,5]
# y = iter(x)
# for x in iter(x):
# 	print(x)


## ploymorphisum  examplee 
# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name
#     def talk(self):              # Abstract method, defined by convention only
#         return 'NotImplementedError("Subclass must implement abstract method")'

# class Cat(Animal):
#     def talk(self):
#         return 'Meow!'

# class Dog(Animal):
#     def talk(self):
#         return 'Woof! Woof!'

# animals = [Cat('Missy'),
#            Cat('Mr. Mistoffelees'),
#            Dog('Lassie')]

# for animal in animals:
#     print (animal.name + ': ' + animal.talk())






# l = []

# import pickle

# # f  = open('kill.pickle','wb')

# # pickle.dump(l,f)
# # f.close()


# k = open('kill.pickle', 'rb')
# s = pickle.load(k)
# print(s)

# d1 = [1,2,3,4]
# d2 = d1
# d2[1] = 8
# print(d2)
# import copy
# d3 = [1,2,3,[6,7]]
# d4 = copy.copy(d3)
# # d4[0]=9
# # print(d4)
# # print(d3)
# d4[3][0] = 8
# print(d3)

# import copy
# d3 = [1,2,3,[6,7]]
# d4 = copy.deepcopy(d3)
# # d4[0]=9
# # print(d4)
# # print(d3)
# d4[3][0] = 8
# print(d3)
# print(d4)
# k = iter(d4)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# l = []
# f = open('intro.txt','r')
# for x in f.readlines():
# 	print(x)

# l2 = set(l)
# for x in l2:
# 	print(x,l.count(x))
# from collections import Counter
# cnt = Counter(f.read().split(' '))
# # print(cnt)
# for x in cnt.items():
# 	print(x[0], x[1])
# # if 'anil' in f.read():
# # 	print(f.read())


# class hello(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, val):
# 		super(hello, self).__init__()
# 		self.val = val
# 		print(self.val)

# 	def display(self):
# 		print('helooo',self.j,self.val)

# h = hello(2)
# # print(h.arg)
# h.j = 4
# print(dir(h))
# h.display()
