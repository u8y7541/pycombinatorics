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

# Test cases
print(gcd(72, 60))  					   # What is the greatest number which is a factor of 60 and 72?
print(lcm(72, 60))  					   # What is the minimum number divisible by 60 and 72?
print(factorial(5)) 					   # How many ways can five people be arranged in a line?
print(nCr(8, 2))    					   # How many ways can you choose two board members from a council of eight?
print(nPr(8, 2))    					   # How many ways can you choose a president and a vice president from a club of eight people?
print(ballsBoxes(10, 3, False)) 			   # How many ways can you choose three positive integers which add up to 10?
print(ballsBoxes(10, 3, True)) 				   # How many ways can you choose three nonnegative integers which add up to 10?
print(solveTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))  # Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. List all the pairs [i, j when the product i * j is even.
print(countTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))  # Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. How many ways can the product of the two numbers be even?
print(probTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0'))   # Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. What is the chance that the product is even?
