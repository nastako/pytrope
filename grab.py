#!/usr/bin/env python3

# example usage: `./grab.py NarrativeTropes`

# this script will try to download and store lists of tropes from
# tvtropes.org, given a page name like 'NarrativeTropes'. if
# successful, it will store them with a filename like 'NarrativeTropes.json'.

# this script ships with another one named `trope.py` which outputs
# a random number of tropes. if the name provided to `tropes.py` is
# not found, it will attempt to call this script in order to download
# the tropes. therefore, `tropes.py` is a more useful script, however
# this script is still useful if you're just looking to download
# lists of tropes.

# TODO : add proper command line flags, instead of argv

import sys
from bs4 import BeautifulSoup
import urllib.request
import json

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://tvtropes.org/pmwiki/pmwiki.php/Main/{page}"

# this is a filter for bs4's find_all that will exclude list items
# that have the 'plus' class, often found in semi-related listings
# on the pages we're grabbing.
def not_plus(c):
	return c != 'plus'

# this function gets the html source of the page
def getPage(name):
	req = urllib.request.Request(url.format(page=name), headers=headers)
	return urllib.request.urlopen(req).read()

# gets the main article content of a page
def get_main_article(page):
	soup = BeautifulSoup(page, 'html.parser')
	return soup.find(id='main-article')

# finds list items that don't have the class 'plus'
def find_no_plus(article):
	return [x.a.get_text() for x in article.find_all('li', class_=not_plus)]

# finds list items that have the class 'plus'
def find_plus(article):
	return [x.a.get_text() for x in article.find_all('li')]

# returns if a list is empty
def is_empty(lst):
	return len(lst) == 0

def main(name):
	try:
		page = getPage(name)
	except:
		# this is a lazy way to deal with bad page gets
		# TODO: improve it!
		print("Error: couldn't get page '{page}'".format(page=name))
		quit(1)

	main = get_main_article(page)

	# tvtropes pages sometimes list items with the 'plus' class and
	# sometimes without it. if our bs4 query returns zero elements
	# we try searching for them again with the 'plus' class.
	items = find_no_plus(main)
	if is_empty(items):
		print("Switching to 'plus' mode...")
		items = find_plus(main)
		if is_empty(items):
			print("Error: no list items found")
			quit(1)

	print("Writing found items to {name}.json...".format(name=name))
	with open("{name}.json".format(name=name), 'w') as f:
		f.write(json.dumps(items, indent=4))

if __name__ == "__main__":
	# this script will only operate if there's one argument (the page name)
	# passed to it
	if (len(sys.argv) - 1) == 1:
		main(sys.argv[1])