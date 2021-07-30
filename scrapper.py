from input_parser import url_maker
from bs4 import BeautifulSoup, SoupStrainer
import requests, lxml.html
from selenium import webdriver


#####################################
# using requests failed due to      #
#           403 error               #
#                                   #
#####################################
#									#
#	ask for anime, return urls		#
#									#
#####################################

# go to login page and get session token
print("logging in...\n")

s = requests.Session()
#s = webdriver.Firefox()


# fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
# s = webdriver.Firefox(firefox_options=fireFoxOptions)


def login():
	login = s.get('https://gogoanime.vc/login.html')
	login_html = lxml.html.fromstring(login.text)
	hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
	form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
	#print(form)

	# fills out form for session

	form['email'] = 'ghidra42@gmail.com'
	form['password'] = 'gogoanime'
	response = s.post('https://gogoanime.vc/login.html', data=form)
login()
print("Your all logged in chief!!!\n")

# asks for user input of the anime wanted 
anime = input("Enter anime name(no special char):> \n")

# asks for the number of episodes available for the anime
episodes = input("Enter the number of episodes:> \n")

# prints out all urls

urls = url_maker(anime, episodes)

print('getting site data...\n')
for url in urls:
	

#####################################
#									#
#	go to url and get download link #
#									#
#####################################

	
	source = s.get(url).text
	soup = BeautifulSoup(source, "lxml")	
	dl = SoupStrainer(class_="list_dowload")
	dl_link = SoupStrainer("a")
	dl_link_block = BeautifulSoup(source, "lxml", parse_only=dl).prettify()
	block = BeautifulSoup(dl_link_block, "lxml", parse_only=dl_link)
	
	tags = block.find_all('a')

	options = []
	links = []
	for t in tags:
		options.append(t.get_text())

	for tag in tags:
		links.append(tag.get('href'))
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

	def let_user_pick(options):
	    print("Please choose:")
	    for idx, element in enumerate(options):
	        print("{}) {}".format(idx+1,element))
	    i = input("Enter number: ")
	    try:
	        if 0 < int(i) <= len(options):
	            
	            print(options[int(i)-1])
	            #print(links[int(i)-1])
	            # re = Request(url=links[int(i)-1], headers=network_headers) 
	            # html = urlopen(re)#.read()
	            post = s.get(links[int(i)-1], headers=hdr)
	            print(post.status_code)
	            # if s.status_code == 200:
	            # 	print(post.text)

	    except:
	        pass
	let_user_pick(options)


	


###########################

	



     
# def test():
# 	html_doc = '''
# [<a href="https://gogo-cdn.com/download.php?url=aHR0cHM6LyAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtert9AdrefsdsdfwerFrefdsfrersfdsrfer36343534jZG4xMS5hbmljZG4uc3RyZWFtL3VzZXIxMzQyLzRmNjNhODUzNzdjZDRjZDQ0YTNlN2ZkMjI2ODFhNGUzL0VQLjEudjEuMzYwcC5tcDQ/dG9rZW49Wm9TeGhaaUViRGZnT1NRVEVZcTJOdyZleHBpcmVzPTE2MjY5NzI0MDUmaWQ9MzE4OTAmdGl0bGU9KDY0MHgzNjAtZ29nb2FuaW1lKXRvLWxvdmUtcnUtZXBpc29kZS0xLm1wNA==">
#    640x360
#   </a>, <a href="https://gogo-cdn.com/download.php?url=aHR0cHM6LyAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtert9AdrefsdsdfwerFrefdsfrersfdsrfer36343534jZG4xMS5hbmljZG4uc3RyZWFtL3VzZXIxMzQyLzRmNjNhODUzNzdjZDRjZDQ0YTNlN2ZkMjI2ODFhNGUzL0VQLjEudjEuNDgwcC5tcDQ/dG9rZW49dlRhM0taVU9ZSWZyNEFfZ0Q3VzlNUSZleHBpcmVzPTE2MjY5NzI0MDUmaWQ9MzE4OTAmdGl0bGU9KDg1NHg0ODAtZ29nb2FuaW1lKXRvLWxvdmUtcnUtZXBpc29kZS0xLm1wNA==">
#    854x480
#   </a>, <a href="https://gogo-cdn.com/download.php?url=aHR0cHM6LyAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtert9AdrefsdsdfwerFrefdsfrersfdsrfer36343534jZG4xMS5hbmljZG4uc3RyZWFtL3VzZXIxMzQyLzRmNjNhODUzNzdjZDRjZDQ0YTNlN2ZkMjI2ODFhNGUzL0VQLjEudjEuNzIwcC5tcDQ/dG9rZW49NmExRkVRQ3p4NDY5dHZJUDZ6a25MZyZleHBpcmVzPTE2MjY5NzI0MDUmaWQ9MzE4OTAmdGl0bGU9KDEyODB4NzIwLWdvZ29hbmltZSl0by1sb3ZlLXJ1LWVwaXNvZGUtMS5tcDQ=">
#    1280x720
#   </a>, <a href="https://gogo-cdn.com/download.php?url=aHR0cHM6LyAawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtert9AdeqwrwedffryretgsdFrsftrsvfsfsrjZG4xMS5hbmljZG4uc3RyZWFtL3VzZXIxMzQyLzRmNjNhODUzNzdjZDRjZDQ0YTNlN2ZkMjI2ODFhNGUzL0VQLjEudjEuMTA4MHAubXA0P3Rva2VuPVRfWE9qRHM5SlRGVVM5YkctVWI1OVEmZXhwaXJlcz0xNjI2OTcyNDA1JmlkPTMxODkwJnRpdGxlPSgxOTIweDEwODAtZ29nb2FuaW1lKXRvLWxvdmUtcnUtZXBpc29kZS0xLm1wNA==">
#    1920x1080
#   </a>]
# 	'''

	
# 	soup = BeautifulSoup(html_doc, "lxml")
# 	tags = soup.find_all('a')
# 	#print(tags)
# 	options = []
# 	for b in tags:
# 		options.append(b.get_text())
	

# 	# for t in tags:
# 	# 	a = t.get_text()
# 	# 	if a == "\n   480x360\n  ":
# 	# 		print("resolution found!!"+a)
# 	# 	elif a == "\n   640x360\n  ":
# 	# 		print("resolution found!!"+a)
# 	# 	elif a == "\n   854x480\n  ":
# 	# 		print("resolution found!!"+a)
# 	# 	elif a == "\n   1280x720\n  ":
# 	# 		print("resolution found!!"+a)
# 	# 	elif a == "\n   1920x1080\n  ":
# 	# 		print("resolution found!!"+a)

	

# 	def let_user_pick(options):
# 	    print("Please choose:")
# 	    for idx, element in enumerate(options):
# 	        print("{}) {}".format(idx+1,element))
# 	    i = input("Enter number: ")
# 	    try:
# 	        if 0 < int(i) <= len(options):
	            
# 	            print(options[int(i)-1])
# 	    except:
# 	        pass
	   

# 	let_user_pick(options)

# test()

	
	

