class HappyNumbers:
    """ Solves the happy numbers challenge. See 
    https://www.codeeval.com/open_challenges/39/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> hn = HappyNumbers()
        >>> numbers = hn.readinput('input.txt')
        >>> len(numbers)
        3
        >>> numbers[0]
        1
        >>> numbers[1]
        7
        >>> numbers[2]
        22
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def happynumber(self, number):
        """ Calculates happy number value. Grumpy Cat does not approve.
        
        Test:
        >>> hn = HappyNumbers()
        >>> hn.happynumber(1)
        1
        >>> hn.happynumber(7)
        1
        >>> hn.happynumber(22)
        0
        """
        known = []
        result = 0
        current = number
        while not result and current not in known:
            known.append(current)
            current = self.squaresumdigits(current)
            if current == 1:
                result = 1
        return result
        
    def happynumberall(self, numbers):
        """ Calculates happy number value for all numbers in list.
        
        Test:
        >>> hn = HappyNumbers()
        >>> hn.happynumberall([1, 7, 22])
        [1, 1, 0]
        """
        result = []
        for number in numbers:
            result.append(self.happynumber(number))
        return result
        
    def squaresumdigits(self, number):
        """ Calculates the sum of the square of the digits of number. 
        
        Test:
        >>> hn = HappyNumbers()
        >>> hn.squaresumdigits(1)
        1
        >>> hn.squaresumdigits(7)
        49
        >>> hn.squaresumdigits(22)
        8
        """
        sum = 0
        while number:
            number, remainder = divmod(number, 10)
            sum += remainder ** 2
        return sum
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        hn = HappyNumbers()
        numbers = hn.readinput(sys.argv[1])
        result = hn.happynumberall(numbers)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()