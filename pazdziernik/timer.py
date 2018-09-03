from zadanie1 import father_twice_old
from zadanie2 import check_duplicates
from zadanie3 import pascal_triangle
from zadanie4 import find_last_chair
from zadanie5 import hashtag_generator
import time
import random


def father_son_data(n):
	def generator(left, right):
		return random.randrange(left, right)

	father_son = []
	for _ in range(n):
		father_son.append([generator(40, 100), generator(1, 35)])
	return father_son

def check_duplicates_data(n):
	strings = ['alfa', 'beta', 'gamma', 'delta', 'epsilon', 'dzeta', 'eta', 'theta', 'jota', 'kappa', 'lambda', 'my', 'ny', 'ksi', 'omikron', 'pi', 'rho', 'sigma', 'tau', 'ipsylon', 'phi', 'chi', 'psi', 'omega']
	choices = [x for x in range(20, 50)]	
	duplicates = [ ]
	for i in range(n):
		duplicates.append(' '.join([random.choice(strings) for _ in range(random.choice(choices))]))
	return duplicates

def generator_for_pascal_and_chair(n, left, right):
	data = [ ]
	for i in range(n):
		data.append(random.randrange(left, right))
	return data

def hashtag_data(n):
	def data_reader():
		data = []
		with open('en') as f:
			for line in f:
				data.append(line[:-1])
		return data

	x = data_reader()
	x.append('            ')
	choices = [y for y in range(3, 35)]
	datasets = [ ]	
	for i in range(n):
		datasets.append(' '.join([random.choice(x) for _ in range(random.choice(choices))]))
	return datasets



if __name__ == '__main__':
	main_time_start = time.time()
	father_son = father_son_data(100000)
	print('father_twice_old data generated in %s seconds' % round((time.time() - main_time_start), 2))

	time_start = time.time()
	duplicates = check_duplicates_data(100000)
	print('check_duplicates data generated in %s seconds' % round((time.time() - time_start), 2))
	
	time_start = time.time()
	pascal = generator_for_pascal_and_chair(100000, 4, 50)
	print('pascal_triangle data generated in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	last_chair = generator_for_pascal_and_chair(100000, 10, 200)
	print('find_last_chair data generated in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	hashtags = hashtag_data(100000)
	print('hashtag_generator data generated in %s seconds' % round((time.time() - time_start), 2))
	
	print('All data generated in %s seconds' % round((time.time() - main_time_start), 2))

	time.sleep(1)
	time_start = time.time()
	ages = []
	for age in father_son:
		ages.append(father_twice_old(age[0], age[1]))
	print('father_twice_old done in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	dupl = [] 
	for duplicate in duplicates:
		dupl.append(check_duplicates(duplicate))
	print('check_duplicates done in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	pasc_trian = []
	for dimension in pascal:
		pasc_trian.append(pascal_triangle(dimension))
	print('pascal_triangle done in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	chair = []
	for number in last_chair:
		chair.append(find_last_chair(number))
	print('find_last_chair done in %s seconds' % round((time.time() - time_start), 2))

	time_start = time.time()
	hasht = []
	for hashtag in hashtags:
		hasht.append(hashtag_generator(hashtag))
	print('hashtag_generator done in %s seconds' % round((time.time() - time_start), 2))
	
	print('Script was working for %s seconds' % round((time.time() - main_time_start), 2))

