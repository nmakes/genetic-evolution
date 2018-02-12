from random import randint

chromosome_size = 128

def random_chromosome(size):
	if size <= 0:
		print "ERROR: CHROMOSOME SIZE SHOULD BE POSITIVE"
		return ""
	else:
		rc = str(bin(randint(0, 2**size)))[2:]
		while len(rc)<size:
			rc += '0'

		return rc

def score(X):
	pass

for i in range(6):
	c = random_chromosome(i**3)
	print
	print c
	print len(c), '/', i**3
	print