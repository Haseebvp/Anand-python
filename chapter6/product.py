# Implement a function product to multiply 2 numbers recursively using + and - operators only
def product(nom,denom):
	if denom==0:
		return 0
	else:
		return nom+product(nom, denom-1)
print product(2,10)
