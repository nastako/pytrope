#!/usr/bin/env python3

# example usage: `./format.py my_data.txt`

# This script will parse a text file and will write the contents of that file
# to a json one. It will pretty it up a little bit on the way, by removing
# extra spaces as well as by ignoring lines that don't contain any letters.

# This script was written as a fast way to convert large lists of tropes that
# I copied from tvtropes.org into json files that can be easily manipulated.

# example command line usage: `./format.py file1.txt file2.txt file3.txt`

import sys
import json
import os

# gives the number of command line arguments used
def argsLen():
	return len(sys.argv) - 1

def main(files):
	for file in files:
		if not file.endswith(".txt"):
			print("{filename} is not a text file. Skipping . . .".format(filename=file))
		else:
			print("Processing {filename}".format(filename=file))
			
			lines = []
			
			with open(file, 'r', encoding="utf-8") as f:
				lines = f.read().strip().split("\n")

			lines = list({line.strip(' \t') for line in lines})
			lines.sort()

			for line in lines:
				if line == "" or line.isspace() or not any(c.isalpha() for c in line):
					lines.remove(line)

			print("Writing {filename}".format(filename=file.replace(".txt", ".json")))
			with open(file.replace(".txt", ".json"), 'w') as f:
				f.write(json.dumps(lines, indent=4))

			print("Deleting source file!")
			os.remove(file)

if __name__ == "__main__":
	if argsLen() >= 1:
		main(sys.argv[1:])
	else:
		print("Error: no arguments provided.")