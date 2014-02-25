class SelfDescribingNumbers:
    """ Solves the self describing numbers challenge. See 
    https://www.codeeval.com/open_challenges/40/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> sd = SelfDescribingNumbers()
        >>> numbers = sd.readinput('input.txt')
        >>> len(numbers)
        3
        >>> numbers[0]
        2020
        >>> numbers[1]
        22
        >>> numbers[2]
        1210
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def isselfdescribing(self, number):
        """ Calculates if number is self describing.
        
        Test:
        >>> sd = SelfDescribingNumbers()
        >>> sd.isselfdescribing(2020)
        1
        >>> sd.isselfdescribing(22)
        0
        >>> sd.isselfdescribing(1210)
        1
        """
        digits = []
        while number:
            number, remainder = divmod(number, 10)
            digits.append(remainder)
        digits.reverse()
        result = 1
        for index, digit in enumerate(digits):
            count = digits.count(index)
            if digit != count:
                result = 0
                break
        return result
        
    def isselfdescribingall(self, numbers):
        """ Calculates if numbers in list are 
        self describing.
        
        Test:
        >>> sd = SelfDescribingNumbers()
        >>> sd.isselfdescribingall([2020, 22, 1210])
        [1, 0, 1]
        """
        result = []
        for number in numbers:
            result.append(self.isselfdescribing(number))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        sd = SelfDescribingNumbers()
        numbers = sd.readinput(sys.argv[1])
        result = sd.isselfdescribingall(numbers)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()