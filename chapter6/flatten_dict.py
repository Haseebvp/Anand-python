def flatten_dict(dt,x=''):
	output={}
	for k,v in dt.items():
		key=x+k
		if isinstance(v,dict):
			output.update(flatten_dict(v,key+'.'))
		else:
			output[key]=v
	return output
print flatten_dict({'q':1,'r':2,'e':{'a':4,'s':6}}
)		
