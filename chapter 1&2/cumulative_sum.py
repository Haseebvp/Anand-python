#implement cumulative sum of a list
def cumulative_sum(nums):
	result=[]
	for i in range(len(nums)):
		result.append(sum(nums[0:i+1]))
        return result
nums=[1,2,3]
print cumulative_sum(nums)

