# a program center_align.py to center align all lines in the given file.
def centre_align(file):
	a=open(file).readlines()
	s=len(max(f))
	for i in f:
		c=(s-len(i))/2
		print ' '*c+i
print centre_align('/home/has/a.txt')
