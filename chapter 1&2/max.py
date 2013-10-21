#max function of a list
def max(list):
	list.sort()
	return list[-1]
print max([2,5,4,3,1,8,2,4])
