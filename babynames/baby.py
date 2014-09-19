import re
import sys

def babynames(htmlfile):

	p=[]
	a=open(htmlfile).read()
	s=re.search(r'\w+\sin\s(\d\d\d\d)',a)
	p.append(s.group(1))
	#print p
	d=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',a)
	d.sort(key= lambda k: k[0])
	for i,j,k in d:
		p.append(j+" "+k+" "+i) 
	print p
	
babynames(sys.argv[1])
