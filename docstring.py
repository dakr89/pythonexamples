

# #  docstring question

# # class kill:
# # 	def docstring(self):
# # 		"""  Hi  this is the example of doc string"""
# # 		print("hello")

# # k = kill()
# # k.docstring()

# # print(k.docstring.__doc__)

# #  how to print a-z letters 
# # import string
# l = [1,2,3,4,1]
# # l1 = [ ord(i) for i in string.ascii_uppercase]
# # print(l1)

# #  map exampless
# # a= 'anil'
# # print(list(map(ord,a)))

# x= map(lambda x,y : x*y,[1,2,3,4],[1,2,3,4])
# print(list(x))
# a = ['one','two']
# c = '_'.join(a)
# print(c)

# # print(set(l))
# # words = ['hi','anil','welcome','anil','kumar']
# # dit = {}
# # for x in words:
# # 	dit[x] = len(x)

# # print(dit)


# a = 'hi anil how r u welcome anil'
# dit = {}
# c = a.split(' ')
# print(c)

# # s = set(c)
# # for x in s:
# # 	dit[x] = a.count(x)

# # print(dit)

# # print( "not emptyy it has values" if dit else "empty dude")

# # with open('abstract.py', 'r') as f:
# # 	for x in f.readline():
# # 		print(x)

# print(sorted(['kumar','anil']))
# k = [1,4,0,6,54,3]
# print(sorted(k))

def test(n = [1,2,4]):
	print(n)
test()
a,b,c = 'anil','kumar','reddy'
s = a + '[' + b + ':' + c + ']'

print(s)

# x = [ y+'s' for y in ['a','b','c']]
# print(x)
import os
def listall(spath):
	for child in os.listdir(spath):
		ss = os.path.join(spath,child)
		if os.path.isdir(ss):
			listall(ss)
		else:
			print(ss)

listall('D:\gitrepos')

# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)

# A2 = sorted([i for i in A1 if i in A0])
# print (A2)

# sorted([A0[s] for s in A0])


# class A(object):
#     def go(self):
#         print("go A go!")
#     def stop(self):
#         print("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")

# class B(A):
#     def go(self):
#         super(B,self).go()
#         print("go B go!")




# b = B()
# b.go()


# print(len('1'))
# print(len(list(map(int,[1,2]))))
# print(list(map(list,['a','b'])))
# print(' '.join(list(map(int,[1,2]))))

# print(len(' '.join(list(map(str, [1.0,2.9])))))

# def test(val):
# 	 a = val + '2'
# 	 a = a *2 
# 	 print(a)
# test("hello")
# l = ['a','b']
# for x in l:
# 	l.append(x.upper())
	     #  3  20  16

	     #  	18

      # 3    4   1
      #      1


# print(l)

# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 2


# print(6/3)
# print(6%3)
# True = False
# print(True)
# def test(*args,**kwargs):

# 	for x in args:
# 		print(x)
# 	for x in kwargs:
# 		print(x)


# test(1,2,3,4,5,{'a':1,'b':3})



# k = {'name':'anil','age':27,'location':'hyderabad'}

# for x,y  in k.items():
# 	print(x ,y)

# k = [{'name':'anil','age':27,'location':'hyderabad'},
# {'name':'kumar','age':27,'location':'banglore'}]


# print(k[0]['age'])
# import copy 
# d1 = [1,2,3]
# d2 = d1
# d2.append(4)
# # print(d1)
# d3 = copy.deepcopy(d2)
# # print(d3)
# d3.append(5)
# print(d2)
# print(d3)

# x = 'anil'

# i = 'a'
# while i in x[:-1]:
# 	print(i)
x = "abcdef"
# i = "a"
# while i in x:
#     x = x[1:]
#     print(i, end = " ")

# x = 'abcd'
# for i in range(len(x)):
#     print(x)
#     x = 'a'

# d = {1,2,3}
# d = d.add(4)
# print(d)
# x = 2
# for i in range(x):
#     x += 1
#     print (x)
# for i in range(10):
#     if i == 5:
#         pass
#     else:
#         print(i)
# else:
#     print("Here")


# x = (i for i in range(3))
# for i in x:
#     print(i)
# for i in x:
#     print(i)

# for i in x:
	# print(i)

# string = 'hii anill'
# for x in string:
# 	print(x ,end=',')
# a = [0, 1, 2, 3]

# # print(a[-1])
# for a[0] in a:

#     print(a[0])
# #     print(a)


# a  = ['anil']
# print(a[-1])
# for x in a:
# 	print(x)
# 	# pass
# a = [0, 1, 2, 3]
# i = -2
# for i noin a:
#     print(i)
#     i += 1



# string = "my name is x"

# print (' '.join(string.split()))
# for i in ' '.join(string.split()):
#     print (i, end=", ")

# print(map(upper,'ab'))
# def to_upper(k):
#     print(k.upper())
# x = ['ab', 'cd']
# print(list(map(to_upper, x)))
# x = ['ab','cd']
# # print(map(len,x))
# print(list(map(list, x)))
# x = [12, 34]
# # # print(list(map(len, x)))
# print(''.join(list(map(str, x))))
# print(' '.join(list(map(str, x))))

# x = [[0], [1]]
# print(' '.join(list(map(str, x))))
x = 123
# print((''.join(list(map(str, x))),'ss'))
# print('abgfyy'.center())
# print("abcdef".center(6))
# print("ab\ncd\nef".expandtabs())
# print("abcdef".find("cd"))
# print("ccdcddcd".find("c"))
# print("Hello {0!s} and {0!s}".format('foo', 'bin'))
# print("Hello {0} and ".format(('foo', 'bin')))

# t = (11,22,3,4)
# print(t[2])
# print('The sum of {0:b} and {1:x} is {2:o}'.format(2, 10, 12))
# print('{:#}'.format(123231231))
# print('xyyxyyxyxyxxy'.replace('xy', '12', 5))
# print('abcd\nefcdghcd'.splitlines())
# print('ab'.zfill(9))
# print(random.randint(3))
# import os
# # print(os.name())
# # print(os.geteuid())

# l1 = [1,2,3,]
# l2 = [1,5,90]
# # l1.append([34,56])
# print([[x, y] for x in range(0, 4) for y in range(0, 4)])





# d1 = {"john":40, "peter":45}

# d2 = {"john":40, "peter":85}
# del d2["john"]
# print(d2)
# t = "jjjej"
# print(3*t)




# try:
# 	print('hello')
# except Exception as e:
# 	print('gelll')
# else:
# 	print('frrr')


# x = open('test.py','r')
# print(x.readline())
# print(1=='1')