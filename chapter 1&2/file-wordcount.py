def char_count(filename):
 f=open(filename).read()
 return len(f)
print char_count('/home/has/a.txt')

def word_count(filename):
 f=open(filename).read()
 return len(f.split())
print word_count('/home/has/a.txt')

def line_count(filename):
 f=open(filename).readlines()
 return len(f)
print line_count('/home/has/a.txt')
