import os
import sys
def list_of_files(dir):
	print os.listdir(sys.argv[1])
print list_of_files(sys.argv[1])
