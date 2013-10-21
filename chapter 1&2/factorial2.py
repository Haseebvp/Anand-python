#To find factorial of a number
def fact(num):
 a=1
 for i in range(1,num+1):
  a=a*i
 return a
print fact(4)
