def exp(x,n):
	if n==0:
		return 1
	else:
		return x*exp(x,n-1)
print exp(5,6)
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
print fact(5)
