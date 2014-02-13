class SumOfDigits:
    """ Solves the sum of digits challenge. See 
    https://www.codeeval.com/open_challenges/21/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> sd = SumOfDigits()
        >>> digits = sd.readinput('input.txt')
        >>> len(digits)
        3
        >>> digits[0]
        23
        >>> digits[1]
        496
        >>> digits[2]
        1211
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def sumdigits(self, number):
        """ Calculate sum of digits of given number.
        See http://stackoverflow.com/a/14940026/1931663
        
        Test:
        >>> sd = SumOfDigits()
        >>> sd.sumdigits(23)
        5
        >>> sd.sumdigits(496)
        19
        >>> sd.sumdigits(1211)
        5
        """
        sum = 0
        while number:
            number, remainder = divmod(number, 10)
            sum += remainder
        return sum
        
    def sumdigitsall(self, number_list):
        """ Find sum of digits of list of numbers
        
        Test:
        >>> sd = SumOfDigits()
        >>> sd.sumdigitsall([23, 496, 1211])
        [5, 19, 5]
        """
        result = []
        for number in number_list:
            result.append(self.sumdigits(number))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        sd = SumOfDigits()
        number_list = sd.readinput(sys.argv[1])
        result = sd.sumdigitsall(number_list)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()