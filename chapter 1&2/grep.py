#: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
def grep(file):
	a=open(file).readlines()
	for i in a:
		if sys.argv[1] in i:
   			print i
print grep('/home/has/a.txt') 
