# pycombinatorics
Easy counting and combinatorics.
Python code to help people do combinatorics problems. Can be used to just do your homework or it can be used in automation. So far, it includes gcd, lcm, factorial, nCr, nPr, the balls and boxes formulae, as well as brute force table counting. Test cases included.
# Installation instructions
As of now, the only way is to copy the file combinatorics.py to your Python3.X/Lib directory. No Py2 port yet.
# Documentation
This is the CPython help generated documentation:

...
NAME
    combinatorics - Combinatorics is a module for easy combinatorics and counting, as the name implies. You can use it for automation or your math homework.

FUNCTIONS
    ballsBoxes(a, b, empty)
        Finds all ways n balls can fit into r boxes, with the argument empty stating if a box can be empty.
        Example combinatorial use: How many ways can you choose three positive integers which add up to 10? (boxes can be empty)
        Example combinatorial use: How many ways can you choose three nonnegative integers which add up to 10? (boxes cannot be empty)
        
        >>> ballsBoxes(10, 3, True)
        66
        >>> ballsBoxes(10, 3, False)
        36
    
    countTable(a, b, condition)
        This function passes its arguments to solveTable() and returns the length of the output. (See documentation for solveTable)
        Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. How many ways can the product of the two numbers be even?
        
        >>> countTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
        7
    
    dynamic_remove(a, *b)
        This function dynamically removes objects from a list. a is the list, b is the removing value. There can be many b values.
        No combinatorial use. It is a utility.
        
        >>> dynamic_remove([1, 2, 3], 2)
        [1, 3]
        >>> dynamic_remove([1, 2, 3], 2, 3)
        [1]
        >>> dynamic_remove([1, 2, 3], 1, 2, 3)
        []
        >>> dynamic_remove([1, 2, 3, 4], 2, 3, 4, 5) # SPECIAL CASE. Will remove objects all b values even if the b value isn't in the list.
        [1]
    
    factorial(a)
        Finds the factorial of the number. It must be a natural number.
        Example combinatorial use: How many ways can five people be arranged in a line?
        
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        >>> factorial(6)
        720
    
    gcd(a, b)
        Finds the greatest common denominator of two numbers using the Euclidean recursive method.
        
        >>> gcd(60, 72)
        12
        >>> gcd(60, 61)
        1
        >>> gcd(12, 12)
        12
    
    lcm(a, b)
        Finds the least common multiple of two numbers by dividing the product by the Euclidean GCD of the two.
        
        >>> lcm(60, 72)
        360
        >>> lcm(3, 4)
        12
        >>> lcm(1, 1)
        1
    
    list_nCr(a, b)
        This function lists all possibilities of nCr given a list of elements and the r value.
        Note: Code is from itertools.combinations. The output is just list(combinations(a, b)). See the docs for itertools.combinations for more help.
        Example combinatorial use: List the ways to choose two numbers from 1 to 10 without replacement where order does not matter.
        
        >>> list_nCr(range(1, 11), 2)
        [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), \
        (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), \
        (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
        >>> list_nCr(range(1, 4), 3)
        [(1, 2), (1, 3), (2, 3)]
        >>> list_nCr([2, 1, 10], 1)
        [(2), (1), (10)]
    
    list_nPr(a, b)
        This function lists all the possibilities of nPr given a list of elements and the r value.
        Note: Code is from itertools.permutations. The output is just list(permutations(a, b)). See the docs for itertools.permutations for more help.
        Example combinatorial use: List the ways to choose two numbers from 1 to 10 without replacement where order matters.
        
        >>> list_nPr(range(1, 11), 2)
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), \
        (2, 10), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), \
        (4, 9), (4, 10), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), \
        (6, 8), (6, 9), (6, 10), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (7, 10), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), \
        (8, 6), (8, 7), (8, 9), (8, 10), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 10), (10, 1), (10, 2), (10, 3), (10, 4), \
        (10, 5), (10, 6), (10, 7), (10, 8), (10, 9)]
        >>> list_nPr(range(1, 4), 3)
        [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
        >>> list_nPr([2, 1, 10], 1)
        [(2), (1), (10)]
    
    mul(...)
        mul(a, b) -- Same as a * b.
    
    nCr(a, b)
        Finds the binomial coefficient of the two numbers, or in other words "n choose r." n is the first number, and r is the second number.
        r has to be less than or equal to n. Both numbers have to be natural numbers.
        Example combinatorial use: How many ways can you choose two board members from a council of eight?
        
        >>> nCr(8, 2)
        28
        >>> nCr(8, 1)
        8
        >>> nCr(8, 7)
        1
    
    nPr(a, b)
        Finds how many r-length permutations of a set of n numbers there are. The same input rules as the nCr function apply.
        Example combinatorial use: How many ways can you choose a president and a vice president from a club of eight people?
        
        >>> nPr(8, 2)
        56
        >>> nPr(8, 1)
        8
        >>> nPr(10, 3)
        720
    
    probTable(a, b, condition)
        This function returns a two-element list of [countTable(a, b, condition), len(a) * len(b)]. See documentation for countTable().
        In other words, it will return the probability of the condition occuring in fraction format, [numerator, denominator].
        Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. What is the chance that the product is even?
        
        >>> probTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
        [7, 9]
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    
    solveTable(a, b, condition)
        Given two lists and a condition, this function gets all the pairs of [i, j] from list 1 and list 2 which satisfy the condition.
        The condition must be a string which evaluates to a boolean, and can use the variables i and j.
        Example combinatorial use: Bob chooses a number fom 1 to 3. Alice chooses a number from 2 to 4. List all the pairs [i, j] when the product i * j is even.
        
        >>> solveTable([1, 2, 3], [2, 3, 4], 'i * j % 2 == 0')
        [[1, 2], [1, 4], [2, 2], [2, 3], [2, 4], [3, 2], [3, 4]]
        >>> solveTable(range(1, 51), [None], 'i % 2 == 0') # You don't have to use both variables.
        [[2, None], [4, None], [6, None], [8, None], [10, None], [12, None], [14, None], [16, None], [18, None], [20, None], \
        [22, None], [24, None], [26, None], [28, None], [30, None], [32, None], [34, None], [36, None], [38, None], [40, None], [42, None], \
        [44, None], [46, None], [48, None], [50, None]]
        
        Notice how "None" was added to the end of each pair. Remember that the function returns an [i, j] pair.

DATA
    g = {'__builtins__': <module '__builtins__' (built-in)>, '__cached__':...
    i = 'factorial'
    result = [[1, 2], [1, 4], [2, 2], [2, 3], [2, 4], [3, 2], [3, 4]]

FILE
    c:\users\hidden_for_my_privacy_reasons\documents\github\pycombinatorics\combinatorics.py
...