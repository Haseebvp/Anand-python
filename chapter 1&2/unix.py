import sys
f=open(sys.argv[2]).readlines()
if sys.argv[1]=='head':
	print f[0:10]
elif sys.argv[1]=='tail':
	print f[len(f)-10:len(f)+1]
else:
	print f
