# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # html = urlopen("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
# # print(html)
# # soup = BeautifulSoup(html)
# # # to get particular tag 

# # # ll = soup.find_all('a')
# # # for x in ll:
# # # 	print (x.get('href'))
# # # table = soup.find_all('table')
# # #  to find exact table instead of all se class  name of the table

# # pickle.dump('file.pickle',l=[12,3,34])

# # table = soup.find('table', class_='wikitable sortable plainrowheaders')

# # for row in table.find_all('tr'):
# # 	print(row)

# # import  requests
# # userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
# # resp = requests.post('http://www.mywebsite.com/user', data=userdata)
# # # resp = requests.get('http://www.mywebsite.com/user')
# # print(resp)

# # from urllib.request import urlopen
# # from urllib.request import Request
# # from urllib.parse import urlencode
# # # x = urlopen('https://www.google.com')
# # # print(x.read())
# # # url = 'http://pythonprogramming.net'
# # # values = {'s':'basic',
# # # 		'submit':'search'}
# # # data = urlencode(values)
# # # data = data.encode('utf-8')
# # # req = Request(url,data)
# # # res = urlopen(req)
# # # # print(res.read())
# # # x = urlopen('http://www.google.com/search?q=test')
# # # print(x.read())

# # x = 'https://www.naukri.com'
# # y = {'python-developer':'jobs'}
# # data = urlencode(y)
# # data = data.encode('utf-8')
# # req = Request(x,data)
# # print(req)
# # res = urlopen(req)

# # # print(res.read())

# from bs4 import BeautifulSoup
# ht = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>


# """

# soup = BeautifulSoup(ht,'lxml')
# #  to get tag
# # print(soup.title)
# #  to get title tag text
# # print(soup.title.text)
# #  to get parent tag of particular tag/tag name
# # print(soup.title.parent)
# # print(soup.p.parent.name)

# #  to get class name of the tag
# # print(soup.p['class'])

# #  to find all tags of specified tag it will return result set object
# # print(soup.find_all('p'))
# #  to find particular tag based on attributee
# # print(soup.find('a' ,attrs={'calss':'story'}))
# #  to find childnode data 
# # print(soup.find('p').find('b').text)
# #  get attributes/ text ..etc from a tag

# # for link in soup.find_all('p'):
# # 	if link.find('a'):
# # 		print(link.find('a').text)
# # 		print(link.find('a').get('href'))
# # 	else:
# # 		print('you missed it')
# #  to get entire text from the page

# # print(soup.get_text())

# # soup = BeautifulSoup(open('kill.html'),"lxml")
# # soup = BeautifulSoup("<html>ddadada</html>",'html.parser')
# # soup = BeautifulSoup('dffs&;sdf!','lxml')
# # print(soup)
# # tag = soup.h2
# # tag.name = "anil"
# # tag["class"]= ["one","two"]
# # print(soup.h1.contents)
# # print (len(list(soup.children)))
# # for x in soup.stripped_strings:
# # 	print(x)
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")
soup = BeautifulSoup(html,'html.parser')
# to get particular tag 

all_tables = soup.find('table',attrs={'class':'wikitable'})
# print(all_tables)
a,b,c,d,e,f,g = [],[],[],[],[],[],[]

# for row in all_tables.find_all('tr'):
# 	cell = row.find_all('td')
# 	states = row.find_all('th')
	# if len(cell) == 6:
	# 	a.append(cell[0].find(text=True))
	# 	b.append(states[0].find(text=True))
	# 	c.append(cell[1].find(text=True))
	# 	d.append(cell[2].find(text=True))
	# 	e.append(cell[3].find(text=True))
	# 	f.append(cell[4].find(text=True))
	# 	g.append(cell[5].find(text=True))

# import pandas as pd

# df = pd.DataFrame(a,columns=['Number'])
# df['State'] = b
# df['Admin_Capital'] = c
# df['Legislative_Capital'] = d
# df['Judiciary_Capital'] = e
# df['Year_Capital'] = f
# df['Former_Capital'] = g


d={'x':11,'b':2,'c':7}
print(sorted(d.values()))