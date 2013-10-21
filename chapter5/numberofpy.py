import os
def extension(dir):
	f=os.listdir(dir)
	result=[]
	for i in f:
		if i[-3:]=='.py':
			result.append(i)
	return len(result)
print extension('/home/has/Documents/hasu/chapter2')
			
