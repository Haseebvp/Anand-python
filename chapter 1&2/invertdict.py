def invertdict(d):
	return {value:key for key,value in d.items()}
print invertdict({'x': 1,'y': 2,'z': 3})
