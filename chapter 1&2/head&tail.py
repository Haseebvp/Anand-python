#The head and tail commands take a file as argument and prints its first and last 2 lines of the file respectively.
import sys
a=open(sys.argv[2]).readlines()
if len(a)>=2:
	if sys.argv[1]=='head':
		print a[:2]
	elif sys.argv[1]=='tail':
		print a[-2:]
else:
	print 'number is less'	
	
