# pytrope
A couple of python scripts for pulling trope data off of tvtropes.org. Useful for writers who need quick inspiration!

## `format.py`

Trims and sorts data from the given input file, line by line. The original file will be deleted.

usage: `./format.py data.txt`

input file: 
data.txt
`        this
 is
 3. some
 "данные"`

output file:
data.json
`[
    "\"\u0434\u0430\u043d\u043d\u044b\u0435\"",
    "3. some",
    "is",
    "this"
]`

## `grab.py`

Downloads a list of tropes from a tvtropes.org index page. The file is stored as a json list.

usage: `./grab.py BejeweledTropes`

output file:
BejeweledTropes.json
`[
    "All-Natural Gem Polish",
    "Body to Jewel",
    "Carbuncle Creature",
    "Color-Coded Stones",
    "Crystal Landscape",
    ...`

## `trope.py`

Returns a list of random tropes. If the file has not been downloaded already, this script will attempt to do so, using `grab.py`.

usage: `./trope.py CleanlinessTropes 4`

output: 
`File does not exist! Let's try grabbing it!
Writing found items to CleanlinessTropes.json...
---------TROPES---------
Shower of Love
Ascetic Aesthetic
Sprint Scrubbing
After-School Cleaning Duty`