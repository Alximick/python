#!/usr/bin/env python3
#chmod +x name.py
import sys
import re
from operator import itemgetter

def checkmail(filename):
	"""func check valid mail"""
	f = open(filename)
	lst = []
	dct = {}
	for line in f:
		i = line[0:-1]
		check = re.search(r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$' , i)
		if check:
			j = i.find('@')
			lst.append(i[j+1:])
		else:
			lst.append('error')

	f.close()
	for i in lst:
		if i in dct:
			dct[i] += 1
		else:
			dct[i] = 1
	for i in map(itemgetter(0), sorted(dct.items(), key = itemgetter(1), reverse = True)):
		print (i, dct[i])
def main():
	print (checkmail.__doc__)
	checkmail(sys.argv[1])


if __name__ == '__main__':
	main()