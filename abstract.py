#   this about abstract class 
import abc
from abc import ABC,abstractmethod
#  abc is  predefined module in python if want  make a class as abastract you need to inherit the ABC class from abc module

class abc_class(ABC):
	#  in side abstract calss you can define abstract method and  methods
	@abstractmethod
	def abcmethod1(self):
		pass

	
	def normalmethod(self):
		print('from normal method')


class my_cls(abc_class):
	def abcmethod1(self):
		
		print('this is inheritaded from the abstract class')

mycls = my_cls()

mycls.abcmethod1()

mycls.normalmethod()
