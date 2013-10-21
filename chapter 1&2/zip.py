# an implementation for zip function using list comprehensions.
a=range(3)
b=['a','b','c']
result=[(x,y) for x in a for y in b if a.index(x)==b.index(y)]
print result
