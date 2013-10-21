#a program reverse.py to print lines of a file in reverse order.
import sys
def reverse(filename):
	f=open(filename).readlines()
	f.reverse()
	for i in f:
		print i
print reverse(sys.argv[1])
