import re

def find_dig(string):
	for i in re.findall("[0-9]+", string):
		print(i)
		
find_dig('02323adad3ds3d33d')