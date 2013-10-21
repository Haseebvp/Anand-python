#a function array to create an 2-dimensional array. The function should take both dimensions as arguments.
def array(a1,a2):
	return [[None]*a2 for a1 in range(1,a2)]
a=array(3,2)
a[0][3]=8
print a
