#!/usr/bin/python
import os
import re
import sys
import urllib
import subprocess
def url_sort_key(url):
	match = re.search(r'-(\w+)-(\w+)\.\w+', url)
	if match:
		return match.group(2)
  	else:
  		return url
def read(filename):
	host = 'code.google.com'
  	temp_dict = {}
  	with open(filename) as f:
	  	for line in f:
	  		search = re.search(r'(/edu/\S+)', line)
	  		if search:
	  			path = search.group(1)
	  			if 'puzzle' in path:
	  				temp_dict['http://' + host + path] = 1
	print len(temp_dict)
	return sorted(temp_dict.keys(),key = url_sort_key)
def download_image(filename, urls):
	dir = filename[:filename.index('_')]
	print dir
	if not os.path.exists(dir):
		os.makedirs(dir)
	index = file(os.path.join(dir, 'index.html'), 'w')
  	index.write('<html><body>\n') 
  	i = 0
  	for img_url in urls:
  		local_name = 'img%d' % i + '.jpg'
  		print 'Download...', i + 1, 'in' , len(urls), local_name
  		urllib.urlretrieve(img_url, os.path.join(dir, local_name))
  		index.write('<img src="%s">' % (local_name,))
  		i += 1
 	index.write('\n</body></html>\n')
  index.close()
  subprocess.Popen('open ' + dir + '/index.html', shell = True, stdout = subprocess.PIPE)

def main():

  	args = sys.argv[1:]
  	urls = read(args[0])
  	download_image(args[0], urls)


if __name__ == '__main__':
  	main()