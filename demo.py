from random import randint

chromosome_size = 128

class Problem:

	def __init__(self, fitness, features, maxScore=None):

		self.fitness = fitness # Function to calculate the fitness of the chromosome
		self.features = features # List of genes in order
		self.maxScore = maxScore # Highest possible score


class HighestNumberProblem(Problem):

	def __init__(self, size, maxScore = None, features = None):

		self.size = size
		self.fitness = self.score
		
		if maxScore==None:
			self.maxScore = 2**size - 1
		else:
			self.maxScore = maxScore

		self.features = features


	def score(self, chromosome):

		L = len(chromosome)
		num = '0b' + chromosome
		num = int(num, 2)

		return float(num) / float(self.maxScore)



class GeneticAlgorithm:

	def __init__(self, problem, population):

		self.problem = problem
		self.population = population


	def random_chromosome(self,size):
		if size <= 0:
			print "ERROR: CHROMOSOME SIZE SHOULD BE POSITIVE"
			return ""
		else:
			rc = str(bin(randint(0, 2**size)))[2:]
			while len(rc)<size:
				rc = '0' + rc

			return rc


	def generate_random_population(self, n):

		randpop = {}
		
		i = 1

		while(i<=n):
			c = self.random_chromosome(self.problem.size)
			
			if c not in randpop:
				randpop[c] = self.problem.score(c)
				i += 1
			else:
				continue

		return randpop


	def Crossover(self, p=0.7):
		newPop = sorted(population)


	def Mutate(self, chromosome, p):
		pass


myalgo = GeneticAlgorithm(HighestNumberProblem(40), {})

pop = myalgo.generate_random_population(100)

for key in pop:
	print key, ":", pop[key]