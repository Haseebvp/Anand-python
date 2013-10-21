#a function unique to find all the unique elements of a list.
def unique(elements):
	u=[elements[0]]
	for i in elements:
		if i not in u:
			u.append(i)
	return u
elements=[1,2,1,3]
print unique(elements)
