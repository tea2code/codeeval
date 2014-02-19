class SumOfIntegers:
    """ Solves the sum of integers from file challenge. See 
    https://www.codeeval.com/open_challenges/24/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> si = SumOfIntegers()
        >>> integers = si.readinput('input.txt')
        >>> len(integers)
        2
        >>> integers[0]
        5
        >>> integers[1]
        12
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def sum(self, integers):
        """ Calculate sum of integers in given list.
        
        Test:
        >>> si = SumOfIntegers()
        >>> si.sum([5, 12])
        17
        """
        return sum(integers)
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        si = SumOfIntegers()
        integers = si.readinput(sys.argv[1])
        result = si.sum(integers)
        print(result)
    else:
        import doctest
        doctest.testmod()