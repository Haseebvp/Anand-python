import sys
def tuple_sort(s):
	q=sorted(s,key=lambda x:x[-1])
	print q
	q.reverse()
	print q
print tuple_sort(sys.argv[1])

