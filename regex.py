import re
# # ex:1
## findall/finditer
# fullstring = '''hi my name is Anil and age 28,salary 70000.
# My father name is Ram and age 56 ,salary 100000'''

# #  get all the digits from the above text
# digits = re.findall(r'\d{1,7}',fullstring)
# print (digits)

# get the names( names are in camel case)
# text = re.findall(r'[A-Z][a-z]*',fullstring)
# print(text)

## finditer it will return iterator object 
# text = re.finditer(r'[A-Z][a-z]*',fullstring)
# print([x.group() for x in text])

# # ex:2
## match/search


# search() will find the text in the given String (in the below Anil will apear many  times but search will pick first searched element)

# st_ring = ' This is Anil full name is Anilkumarreddy with surname Anilkumarreddy dappili'
# # text = re.match(r'[A-Z][a-z]*',st_ring)
# text = re.match('Anil',st_ring)
# text = re.search('Anil',st_ring)
# if text:
# 	print(text.group())
# else:
# 	print('no data')

# match() : i the given text is at the begiing og the string it will match other wise None(below example Anil will appear middle of the text so match will return None)

st_ring = 'This is Anil full name is Anilkumarreddy with surname Anilkumarreddy dappili'

# text = re.match('Anil',st_ring)
#  after This one or more space(it should be in begginig of the string)

# text = re.match(r'This\s+',st_ring)

# line = "Cats are smarter than dogs"
# text = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if text:
# 	print(text.group())
# 	# print(text.group(1))
# 	# print(text.group(2))

# else:
# 	print('no data')


# # ex:3
# # sub string 
#  it replace the text "ram " with another word  'RamaKrishnareddy'
# substr = re.sub('Ram','RamaKrishnareddy',fullstring,1)
# print(substr)

#  getting only number from the text
# phone = "2004-959-559 This is Phone Number"
# substr = re.sub(r'[A-Z][a-z].*$','',phone,1)
# #  or 
# # substr = re.sub(r'\D','',phone)
# print(substr)

d1 = [{
    "b": 10
},{"a":29}]

d2 = d1

d2[0]['b'] = 30
d2[1]['a'] = 99

print(d1[0]['b'])
print(d1[1]['a'])

import json
class Foo(object):
	def to_json(self):
		k = self.__getattribute__
		print(k)


class kill(Foo):
	def __init__(self,a,b):
		self.a = a
		self.b = b


k = kill(1,2)
k.to_json()



