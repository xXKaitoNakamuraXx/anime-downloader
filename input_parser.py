
# url of main website
URL = "https://gogoanime.vc/"

# this takes the anime and number of episodes and produces a url to the desires episode of the user

def url_maker(anime, episodes):

	parsed_words = anime.replace(" ", "-")
	episode = int(episodes) 
	num = 0
	urls = []
	while episode > num:
		num += 1
		url_search = parsed_words + "-episode-" + str(num)
		# this is just for seeing the urls
		#print(URL + url_search)
		url = URL + url_search
		urls.append(url)

	return urls
		
	

