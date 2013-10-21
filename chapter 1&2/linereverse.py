def reverse_line(file):
 a=open(file).readlines()
 for i in a:
  print i[::-1]
print reverse_line('/home/has/a.txt')
 
