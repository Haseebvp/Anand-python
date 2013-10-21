import sys
def longer(filenames):
	for f in sys.argv:
		for line in open(f):
			if len(line)>39:
				print line
