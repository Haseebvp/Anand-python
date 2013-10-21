# a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enumerate(a):
	return [(a.index(x),x) for x in a]
a=['a','s','d']
print enumerate(a)
