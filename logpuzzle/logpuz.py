#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


op=[]
def read_urls(filename):
	j= open(filename).readlines()
	for q in j:
		puzzle_url=re.search(r'puzzle',q)
		if puzzle_url:
#			print q
			h=re.search(r'GET (\w*.*) HTTP',q)
			if h:
#				print h.group(1)
				op.append('http://code.google.com'+h.group(1)+'\n')
			#	print  'http://code.google.com'+h.group(1)
				#return 'http://code.google.com'+h.group(1)
	print op			
	def ssoorrtt(op):
		for t in op:
			ty=re.search(r'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-(\w*.\w*)',t)
			if ty:
				return  ty.group(1)
	
	return sorted(op,key=ssoorrtt)
	

"""Returns a list of the puzzle urls from the given log file
 extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  

def download_images(img_urls, dest_dir):
	if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

        s=file(os.path.join(dest_dir, 'index.html'), 'w')
        s.write('<html><body>\n')
        i = 0
        for img_url in img_urls:
               	print urllib.urlretrieve(img_url, os.path.join(dest_dir,'img%d' %i))
                i += 1
                s.write('\n</body></html>\n')
                #s.close()





"""Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
"""
  # +++your code here+++
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
