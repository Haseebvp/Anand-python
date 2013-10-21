#a function dups to find all duplicates in the list.
def dupe(elements):
	d=[]
	for i in range(len(elements)):
		if elements[i] in elements[i+1:] and elements[i] not in d:
			d.append(elements[i])
	return d
elements=[1,2,1,3,2]
print dupe(elements)
