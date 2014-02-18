from math import sqrt

class Fibonacci:
    """ Solves the fibonacci challenge. See 
    https://www.codeeval.com/open_challenges/22/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> f = Fibonacci()
        >>> numbers = f.readinput('input.txt')
        >>> len(numbers)
        2
        >>> numbers[0]
        5
        >>> numbers[1]
        12
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def fibonacci(self, number):
        """ Calculate fibonacci number of given number 
        using Binet's formula.
        See http://mathworld.wolfram.com/FibonacciNumber.html
        
        Test:
        >>> f = Fibonacci()
        >>> f.fibonacci(5)
        5
        >>> f.fibonacci(12)
        144
        """
        sqrtFive = sqrt(5)
        result = ((1 + sqrtFive)**number - (1 - sqrtFive)**number) / (2**number * sqrtFive)
        return int(result) # Prevent small floating point differences.
        
    def fibonacciall(self, number_list):
        """ Calculate fibonacci number of all numbers.
        
        Test:
        >>> f = Fibonacci()
        >>> f.fibonacciall([5, 12])
        [5, 144]
        """
        result = []
        for number in number_list:
            result.append(self.fibonacci(number))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        f = Fibonacci()
        number_list = f.readinput(sys.argv[1])
        result = f.fibonacciall(number_list)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()