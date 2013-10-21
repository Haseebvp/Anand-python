import sys
import urllib
import re
f=urllib.urlopen(sys.argv[1]).read()
s=re.findall(r'http://[\w.]+.+"',f)
for i in s:
	print i[:-1]
sys.argv[1]
