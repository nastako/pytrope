#!/usr/bin/env python3

# example usage `./trope.py NarrativeTropes 4`
#               `./trope.py NarrativeTropes -1`
#               `./trope.py NarrativeTropes`

# This script prints a number of random tropes to the command line
# given a tvtrope.org article name. It's designed for index pages.
# It is not necessary to have the data stored 

import random
import sys
import json
import subprocess

def main(listfile, num):
	data = []
	name = ""

	# this lets us use full or short file names
	if not listfile.endswith(".json"):
		name = listfile
		listfile = listfile + ".json"
	else:
		name = listfile.replace(".json", "")

	# here we try to make sense of the number value provided by the user.
	try:
		num = int(num)
	except ValueError:
		print("invalid input number, defaulting to 1!")
		num = 1
	
	# this tries to open the file
	try:
		with open(listfile, 'r') as f:
			data = json.load(f)
	except FileNotFoundError:
		# ok we didn't find the file, no big deal!
		print("File does not exist! Let's try grabbing it!")
		cp = subprocess.run(["python.exe", "grab.py", name], shell=True)
		if cp.returncode != 0:
			print("Error: could not find file")
			quit(1)
		else:
			with open(listfile, 'r') as f:
					data = json.load(f)

	print("---------TROPES---------")
	if num < 1 or num >= len(data):
		for item in data:
			print(item)
	else:
		random.shuffle(data)

		for i in range(num):
			if i <= (len(data) - 1):
				print(data[i])

if __name__ == "__main__":
	if (len(sys.argv) - 1) == 2:
		main(sys.argv[1], sys.argv[2])
	elif (len(sys.argv) - 1) == 1:
		main(sys.argv[1], 1)