#Implement a function product, to compute product of a list of numbers.
def prod(a):
	t=1
	for i in a:
		t=t*i
	return t

print prod([1,2,3])
