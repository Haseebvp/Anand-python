def read_file(filename):
	return open(filename).read()
def char_count(file):
	count_dict={}
	for ch in file:
		count_dict[ch]=count_dict.get(ch,0)+1
	return count_dict
def main(filename):
	count_dict=char_count(read_file(sys.argv[1]))
	for char,count in count_dict.items():
		if '\n' not in char:
			print char,count
import sys
if __name__ == '__main__':
	main(sys.argv[1])

