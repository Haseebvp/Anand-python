#implement min and max functions in list
def min(list):
	list.sort()
	return list[0]
def max(list):
	list.sort()
	return list[-1]
print min([1,2,3])
print max([1,2,3])
