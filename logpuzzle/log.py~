import os
import re
import sys
import urllib
p=[]
def read_urls(filename):
	f=open(filename).readlines()
        for q in f:
                puzzle_url=re.search(r'puzzle',q)
                if puzzle_url:
                        s=re.search(r'(\w*.*) HTTP',q)
                        if s:
                                p.append('http://code.google.com'+s.group(1)+'\n')
	c=sorted(p)
        print c
def download_images(img_urls,dest_dir):
	if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
        l=file(os.path.join(dest_dir,'index.html'),'w')
        j=0
        for k in img_urls:
                return urllib,urlretrieve(img_urls.os.path.join(det_dir,'img%d'%j))
        j+=1




print read_urls('animal_code.google.com')
print download_images(img_urls, dest_dir)

