import os
import sys
def extcount(dir):
	f=os.listdir(sys.argv[1])
	a=[]
	s={}
	for i in f:
		a.append(i[i.find('.')+1:])
	for j in a:
		s[j]=s.get(j,0)+1
	for key,value in s.items():
		print key,value
extcount(sys.argv[1])
	
