# a,b = 2,3
# l1 = [1,2,3,4,5,6,7,8]
# print(l1[18:])
# y = [x for x in l1 if x%2 == 0]
# print (y)
# def foo(l=[]):
# 	l.append(1)
# 	print(l)
# 	return l 

# foo()
# foo()
# word = 'aeioubcdfg'
# print(word[:3]+word[3:])

# def multipliers ():

#     return [lambda x: i * x for i in range (4)]

# for m in multipliers ():
#  	print(m(2))

f= [lambda x: i*x for i in range(4)]
print(f(2))
