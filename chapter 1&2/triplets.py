#a function triplets
def triplets(a,b):
	return [(x,y,x+y) for x in a for y in b if a.index(x)==b.index(y)]
a=range(4)
b=[4,3,2,1]
print triplets(a,b)
