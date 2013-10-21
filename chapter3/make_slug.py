import re
list=re.findall(r'(\w+)'," --hello-  world--")
print '-'.join(list)

