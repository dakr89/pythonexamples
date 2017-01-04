
def my_decarator(original_fun):
	print('HELLO FROM MY DECRATOR')
	def sub_fnc(*args,**kwargs):
		print('from insidee')
		return original_fun(*args,**kwargs)
	return sub_fnc



@my_decarator
def myfunc(name,age):
	print('hello anil how r ru {},{}',format(name,age))

myfunc('anil','28')


# def parent(num):

#     def first_child():
#         return "Printing from the first_child() function."

#     def second_child():
#         return "Printing from the second_child() function."

#     try:
#         assert num == 10
#         return first_child
#     except AssertionError:
#         return second_child

# foo = parent(10)
# bar = parent(11)
# print(foo())
# print(bar())