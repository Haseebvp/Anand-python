#Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def unique_string(list):
 u=[]
 for i in range(len(list)):
  if list[i].lower() not in u:
   u.append(list[i]) 
 return u
print unique_string(['haseeb','latheef','shihas','latheef','haseeb','haseeb'])
