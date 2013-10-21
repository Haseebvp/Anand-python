#an implementation for filter using list comprehensions.
def filter(a):
	return [x for x in a if x%2==0]
a=range(10)
print filter(a)
