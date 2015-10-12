from functools import reduce
from operator import mul

# Lambdas make them short

gcd = lambda a, b: gcd(*sorted([abs(b - a), min([a, b])])) if a != b else a
lcm = lambda a, b: (a * b) // gcd(a, b)
factorial = lambda a: reduce(mul, range(1, a + 1))
nCr = lambda a, b: reduce(mul, [i for i in range(a, a - b, -1)]) // factorial(b)
nPr = lambda a, b: reduce(mul, [i for i in range(a, a - b, -1)])
ballsBoxes = lambda a, b, empty: nCr(a - 1, b - 1) if not empty else nCr(a + b - 1, b - 1)
solveTable = lambda a, b, condition: [exec('global result; result = []'), [[exec('global result; result.append([i, j])') for j in b if eval(condition, {'i':i, 'j':j})] for i in a], result][-1]
countTable = lambda a, b, condition: len(solveTable(a, b, condition))
probTable = lambda a, b, condition: [countTable(a, b, condition), len(a) * len(b)]


# Documentation

# Lambdas have no name, so assign them all a name
g = globals().copy()
for i in g:
	try:
		g[i].__name__ = i
	except:
		pass

__doc__ = '''Combinatorics is a module for easy combinatorics and counting, as the name implies. You can use it for automation or you math homework.'''
gcd.__doc__ = '''Finds the greatest common denominator of two numbers using the Euclidean recursive method.
				 
				 >>> gcd(60, 72)
				 12
				 >>> gcd(60, 61)
				 1
				 >>> gcd(12, 12)
				 12'''
lcm.__doc__ = '''Finds the least common multiple of two numbers by dividing the product by the Euclidean GCD of the two.
				 
				 >>> lcm(60, 72)
				 360
				 >>> lcm(3, 4)
				 12
				 >>> lcm(1, 1)
				 1'''
factorial.__doc__ = '''Finds the factorial of the number. It must be a natural number.
					   Example combinatorial use: How many ways can five people be arranged in a line?

					   >>> factorial(5)
					   120
					   >>> factorial(10)
					   3628800
					   >>> factorial(6)
					   720'''
nCr.__doc__ = '''Finds the binomial coefficient of the two numbers, or in other words "n choose r." n is the first number, and r is the second number.
				 r has to be less than or equal to n. Both numbers have to be natural numbers.
				 Example combinatorial use: How many ways can you choose two board members from a council of eight?

				 >>> nCr(8, 2)
				 28
				 >>> nCr(8, 1)
				 8
				 >>> nCr(8, 7)
				 1'''
nPr.__doc__ = '''Finds how many r-length permutations of a set of n numbers there are. The same input rules as the nCr function apply.
				 Example combinatorial use: How many ways can you choose a president and a vice president from a club of eight people?

				 >>> nPr(8, 2)
				 56
				 >>> nPr(8, 1)
				 8
				 >>> nPr(10, 3)
				 720'''
ballsBoxes.__doc__ = '''Finds all ways n balls can fit into r boxes, with the argument empty stating if a box can be empty.
						Example combinatorial use: How many ways can you choose three positive integers which add up to 10? (boxes can be empty)
						Example combinatorial use: How many ways can you choose three nonnegative integers which add up to 10? (boxes cannot be empty)

						>>> ballsBoxes(10, 3, True)
						66
						>>> ballsBoxes(10, 3, False)
						36'''
solveTable.__doc__ = '''Given two lists and a condition, this function gets all the pairs of [i, j] from list 1 and list 2 which satisfy the condition.
						The condition must be a string which evaluates to a boolean, and can use the variables i and j.
						Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. List all the pairs [i, j] when the product i * j is even.

						>>> solveTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
						[[1, 2], [1, 4], [2, 2], [2, 3], [2, 4], [3, 2], [3, 4]]
						>>> solveTable(range(1, 51), [None], 'i % 2 == 0') # You don't have to use both variables.
						[[2, None], [4, None], [6, None], [8, None], [10, None], [12, None], [14, None], [16, None], [18, None], [20, None], \
						[22, None], [24, None], [26, None], [28, None], [30, None], [32, None], [34, None], [36, None], [38, None], [40, None], [42, None], \
						[44, None], [46, None], [48, None], [50, None]]

						Notice how "None" was added to the end of each pair. Remember that the function returns an [i, j] pair.'''
countTable.__doc__ = '''This function passes its arguments to solveTable() and returns the length of the output. (See documentation for solveTable)
						Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. How many ways can the product of the two numbers be even?

						>>> countTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
						7'''
probTable.__doc__ = '''This function returns a two-element list of [countTable(a, b, condition), len(a) * len(b)]. See documentation for countTable().
					   In other words, it will return the probability of the condition occuring in fraction format, [numerator, denominator].
					   Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. What is the chance that the product is even?

					   >>> probTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
					   [7, 9]'''

# Test cases
if __name__ == '__main__':
	print(gcd(72, 60))
	print(lcm(72, 60))
	print(factorial(5))
	print(nCr(8, 2))
	print(nPr(8, 2))
	print(ballsBoxes(10, 3, False))
	print(ballsBoxes(10, 3, True))
	print(solveTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))
	print(countTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))
	print(probTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))