from input_parser import url_maker
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

####################################
# Login to site with user creds to #
#       enable downloads           #
####################################

print("Logging In...\n")

# webdriver to use
s = webdriver.Firefox()

# Login 
def login():
	try:
		login = s.get('https://gogoanime.vc/login.html')
		auth = s.find_element_by_name("email")
		auth.clear()
		auth.send_keys("YOUR EMAIL")
		passw = s.find_element_by_name("password")
		passw.clear()
		passw.send_keys("YOUR PASSWORD")
		passw.send_keys(Keys.RETURN)
		print("Your all logged in Chief!!!\n")
	except:
		print("Sorry. Unable to log in under these conditions.")
		s.quit()
		exit()

login()

# asks for user input of the anime wanted and
# asks for the number of episodes wanted for the anime

anime = input("Enter anime name(no special char):> \n")
episodes = input("Enter the number of episodes:> \n")

# prints out all urls
urls = url_maker(anime, episodes)#anime, episodes)

print('Finding Resolutions...\n')
for url in urls:
	

#####################################
#	           		    #
#   go to url and get download link #
#				    #
#####################################
# go to url and parse out resolution 
	s.get(url)
	source = s.page_source
	soup = BeautifulSoup(source, "lxml")	
	dl = SoupStrainer(class_="list_dowload")
	dl_link = SoupStrainer("a")
	dl_link_block = BeautifulSoup(source, "lxml", parse_only=dl).prettify()
	block = BeautifulSoup(dl_link_block, "lxml", parse_only=dl_link)
	
	tags = block.find_all('a')

	options = []
	
	# prettify text for display
	for t in tags:
		o = t.get_text().replace(" ", "").replace("\n", "")
		options.append(o)

	def let_user_pick(options):
	    print("Please choose:")
	    for idx, element in enumerate(options):
	        print("{}) {}".format(idx+1,element))
	    i = input("Enter number: ")
	    try:
	        if 0 < int(i) <= len(options):
	            
	            print(options[int(i)-1])
	            post = s.find_element_by_partial_link_text(options[int(i)-1])
	            post.click()
	            time.sleep(3)
	            pyautogui.keyDown('alt')
	            pyautogui.press('s')
	            pyautogui.keyUp('alt')
	            pyautogui.press('return')

	    except:
	        print('Not available')
	        exit()
	let_user_pick(options)

