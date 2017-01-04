#  you can define  n number of except blocks
# try and except blocks are mandatory
#  else and finally  blocks optional
# Exception is the super class for all errors
# if yo want raise exception use the keyword < raise errorname>
  #       ex : raise ValueError
  #       in except block just define this error like 
  #       except ValueError as ve:
		# print(ve)


import os
try:
	print('from try')
	a = 4/5
	#  if you dont want execute except/finally/else  block just use this
	# os._exit(0)
	f = open('intr.txt','rb')
	if f.name != 'intro.txt':
		raise ValueError
except ValueError as ve:
	print(ve)
except NameError as ne:
	print(ne)
except Exception as e:

	print(e)
	
else:
	print('from else block')

finally:
	print('from final block')


