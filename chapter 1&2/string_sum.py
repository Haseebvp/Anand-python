#What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
def string_sum(a):
	sum=' '
	for i in a:
		sum=str(sum)+str(i)
	return string_sum
print string_sum(['haseeb','latheef'])
