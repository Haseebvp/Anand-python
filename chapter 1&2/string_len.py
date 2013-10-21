def string_len(list):
 a=list.split(' ')
 print a
 s=map(lambda a:len(a),a)
 return s
print string_len('hello world')
 
