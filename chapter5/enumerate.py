def my_enumerate(a):
	for i in range(len(a)):
		yield i,a[i]
x=my_enumerate(['a','b','c','d'])
print x.next()
print x.next()
