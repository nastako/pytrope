#!/usr/bin/env/python3
import json
import random
from bs4 import BeautifulSoup
import urllib.request
import sys

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://tvtropes.org/pmwiki/pmwiki.php/Main/{name}"
trope_folder = "tropes/"

# only ever use this in an `except` block
def get_error():
	return sys.exc_info()[0]

def fix_filename(filename):
	if not filename.lower().endswith(".json"):
		filename = filename + ".json"
	return filename

def io(filename, data={}, mode='r'):
	filename = trope_folder + fix_filename(filename)
	error = None
	try:
		with open(filename, mode, encoding="utf-8") as f:
			if mode == 'r':
				data = json.load(f)
			elif mode == 'w':
				f.write(json.dumps(data, indent=4))
	except:
		data = {}
		error = get_error()
	return data, error

def update(name):
	data = {}
	error = None
	try:
		request = urllib.request.Request(url.format(name=name), headers=headers)
		page = urllib.request.urlopen(request).read()
		soup = BeautifulSoup(page, 'html.parser').find(id='main-article')
		data = get_tropes(soup, f=lambda c: c != "plus")
		if len(data) == 0:
			data = get_tropes(soup)
	except:
		error = get_error()
	return data, error

def get_number(num):
	error = None
	try:
		num = int(num)
	except:
		num = 1
		error = get_error()
	return num, error

def print_data(data, num):
	num, error = get_number(num)
	keys = list(data.keys())

	if num < 0 or num >= len(data):
		for item in keys:
			print(data[item])
	else:
		random.shuffle(keys)

		while num > 0:
			key = keys.pop()
			print(data[key])
			num = num - 1

def get_tropes(soup, f=None):
	return {x.a.get_text() : x.get_text() for x in soup.find_all("li", _class=f)}

def main(file, num):
	p, e = io(file, mode='r')
	if e != None:
		p, e = update(file)
		if e == None:
			io(file, p, mode='w')
	print_data(p, num)

if __name__ == "__main__":
	if (len(sys.argv) - 1) == 2:
		main(sys.argv[1], sys.argv[2])
	elif (len(sys.argv) - 1) == 1:
		main(sys.argv[1], 1)
	else:
		print("error: no arguments provided")