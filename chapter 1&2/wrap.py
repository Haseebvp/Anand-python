#a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
def wrap(file):
	key=int(sys.argv[2])
	f=open(file).readlines()
	for i in f:
		new=i
  		while len(new)>key:
    			print new[:k]
			new=new[k:]
		print new
print wrap('/home/has/a.txt')

					
