# pytrope
A couple of python scripts for pulling trope data off of [TV Tropes](https://tvtropes.org). Useful for writers who need quick inspiration!

## Installation

pytrope requires Python 3. It might support earlier versions of python in the future, but at this point I don't care, and Python 3 has been out for over ten years, so you should really be using it.

Just run the `install.sh` file and it will use pip3 to install the html parser.

# Usage

`./trope.py CleanlinessTropes 4`

This will return 4 random tropes from the Cleanliness Tropes index on TVTropes.org. Currently, you have to have previous knowledge of likely index pages, as pytrope won't search or provide suggestions for what you're actually trying to find. TvTropes has an IndexIndex page that could probably be used for this purpose, but it's not currently supported.
