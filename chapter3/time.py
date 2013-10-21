import sys
import os
def stat(dir):
	f=os.listdir(sys.argv[1])
	for i in f:
		print i,len(open(os.path.abspath(sys.argv[1]+'/'+i)).readlines()),os.stat(os.path.abspath(sys.argv[1]+'/'+i))[8]
stat(sys.argv[1])
