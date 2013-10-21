import urllib
import sys
import re
def antihtml(url):
	urllib.urlretrieve(sys.argv[1],'web')
	a=re.findall(r'>[^<]+<',open('web').read())
	for i in a:
		print i[1:-1]
antihtml(sys.argv[1])	
