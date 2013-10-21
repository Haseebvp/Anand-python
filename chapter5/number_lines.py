import os
def number(dir):
	f=os.listdir(dir)
	for files in f:
		a=open(files).readlines()
	print len(a)
print number('/home/has/c')
