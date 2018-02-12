def test_random_chromosome():
	for i in range(6):
		c = random_chromosome(i**3)
		print
		print c
		print len(c), '/', i**3
		print