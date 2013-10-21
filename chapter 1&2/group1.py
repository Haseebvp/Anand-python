# a function group(list, size) that take a list and splits into smaller lists of given size.
def group(l,num):
	return[l[i:i+num] for i in range(0,len(l),num)]
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
