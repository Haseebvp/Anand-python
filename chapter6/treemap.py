#a function treemap to map a function over nested list.
def treemap(l):
	for i in l:
		if isinstance(i,list):
			treemap(i)
		else:
			p=l.index(i)
			l.remove(l[p])
			l.insert(p,i*i)
	return l
print treemap([1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]
