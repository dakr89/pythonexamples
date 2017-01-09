
# def my_decarator(original_fun):
# 	print('HELLO FROM MY DECRATOR')
# 	def sub_fnc(*args,**kwargs):
# 		print('from insidee')
# 		return original_fun(*args,**kwargs)
# 	return sub_fnc



# @my_decarator
# def myfunc(name,age):
# 	print('hello anil how r ru {},{}',format(name,age))

# myfunc('anil','28')


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






# def main_method(func):
# 	def edit_text(name):
# 		 return '<p> {} </p>'.format(func(name))
# 	return edit_text


# def div_method(func):
# 	def edit_text2(name):
# 		return "<div>  {}  </div>".format(func(name))
# 	return edit_text2


# def strong_method(func):
# 	def edit_text3(name):
# 		return "<strong><i>  {}  </i></strong>".format(func(name))
# 	return edit_text3



# @div_method
# @strong_method
# @main_method

# def mytext(name):
# 	return " Hi my name is {}".format(name)

# print(mytext('anil'))

#  decarating method  example
# def myfunc(func):
# 	def my_sud_func(*args, **kwargs):
# 		return "<p> {} </p>".format(func(*args, **kwargs))
# 	return my_sud_func



# class test:
# 	def __init__(self,name,location):
# 		self.name = name
# 		self.location = location

# 	@myfunc
# 	def my_decarator(self):
# 		return " hy my name is {0}  from {1}".format(self.name,self.location)


# t = test('anil','hyderabad')
# print(t.my_decarator())


# passing argument to decartor
# def parameter(variable):
# 	def myfunc(func):
# 		def my_sud_func(*args, **kwargs):
# 			return "<p> {1}   {0}</p>".format(variable,func(*args, **kwargs))
# 		return my_sud_func
# 	return myfunc



# class test:
# 	def __init__(self,name,location):
# 		self.name = name
# 		self.location = location

# 	@parameter('change nice work superb !!!!!')
# 	def my_decarator(self):
# 		return " hy my name is {0}  from {1}".format(self.name,self.location)


# t = test('anil','hyderabad')
# print(t.my_decarator())

#  useing the module wrap
#   if u use @wraps(function) it will give exact function name which we are decarting
#   here  we are  decarationg the function my_decarator as paramenter myfunc
from functools import wraps

def parameter(variable):
	def myfunc(func):

		@wraps(func)
		def my_sud_func(*args, **kwargs):
			""" hi this is wrap example"""
			return "<p> {1}   {0}</p>".format(variable,func(*args, **kwargs))
		return my_sud_func
	return myfunc



@parameter('change nice work superb !!!!!')
def my_decarator(name,location):
	""" hi this is from decarator func"""
	return " hy my name is {0}  from {1}".format(name,location)


print(my_decarator("anil","hyderabad"))
print(my_decarator.__name__)
print(my_decarator.__doc__)
print(my_decarator.__module__)

