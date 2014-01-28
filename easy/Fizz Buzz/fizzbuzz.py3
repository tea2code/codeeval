import sys

class FizzBuzz:
    """ Solves the Fizz Buzz test for arbitrary input according to 
    https://www.codeeval.com/open_challenges/1/. 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    
    Member:
    params -- List of tubles which contain the three Fizz Buzz parameter A, B, N (list).
    """
    
    DELIMITER = ' '
    
    def __init__(self):
        self.params = []
    
    def prettyprint(self, solution):
        """ Prints a solution. Can take a single solution or a list of 
        solutions. 
        
        Test:
        >>> fb = FizzBuzz()
        >>> fb.prettyprint(['1', 'F', 'B', 'F', '5', 'FB'])
        1 F B F 5 FB
        >>> fb.prettyprint([['1', 'F', 'B', 'F', '5', 'FB'], ['1', 'F', 'B', 'F', '5', 'FB']])
        1 F B F 5 FB
        1 F B F 5 FB
        """
        if solution and not isinstance(solution[0], list):
            solution = [solution]
        for s in solution:
            line = ''
            for value in s:
                line += value + self.DELIMITER
            line = line.strip(self.DELIMITER)
            print(line)
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> fb = FizzBuzz()
        >>> fb.readinput('input.txt')
        >>> len(fb.params)
        3
        >>> fb.params[0]
        (3, 5, 10)
        >>> fb.params[1]
        (2, 7, 15)
        >>> fb.params[2]
        (2, 3, 10)
        """
        with open(file_name) as file:
            for line in file.readlines():
                params = map(int, line.split(self.DELIMITER))
                self.params.append(tuple(params))       

    def solve(self, a, b, n):
        """ Solves a fizz buzz quiz. Returns a list of result. 
        
        Test:
        >>> fb = FizzBuzz()
        >>> fb.solve(3, 5, 15)
        ['1', '2', 'F', '4', 'B', 'F', '7', '8', 'F', 'B', '11', 'F', '13', '14', 'FB']
        """
        results = []
        for i in range(1, n + 1):
            result = ''
            if i % a == 0:
                result += 'F'
            if i % b == 0:
                result += 'B'
            if not result:
                result = str(i)
            results.append(result)
        return results
        
    def solveAll(self):
        """ Solves all fizz buzz quiz. Returns list of lists. 
        
        Test:
        >>> fb = FizzBuzz()
        >>> fb.params = [(3, 5, 15), (2, 3, 6)]
        >>> fb.solveAll()
        [['1', '2', 'F', '4', 'B', 'F', '7', '8', 'F', 'B', '11', 'F', '13', '14', 'FB'], ['1', 'F', 'B', 'F', '5', 'FB']]
        """
        result = []
        for param in self.params:
            result.append(self.solve(param[0], param[1], param[2]))
        return result
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        fb = FizzBuzz()
        fb.readinput(sys.argv[1])
        solution = fb.solveAll()
        fb.prettyprint(solution)
    else:
        import doctest
        doctest.testmod()