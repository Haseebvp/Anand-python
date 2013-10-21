#cumulative product of a list
def cumulative_product(nums):
	key=1
	l=[]
	for i in nums:
		key=key*i
		l.append(key)
	return l
nums=[1,2,3]
print cumulative_product(nums)
