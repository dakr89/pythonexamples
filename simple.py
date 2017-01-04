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






name = 'aas'
if name:
	raise Exception('get losee')







