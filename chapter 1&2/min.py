#min function of a list
def min(list):
	list.sort()
	return list[0]
print min([2,5,3,6,4,1])
