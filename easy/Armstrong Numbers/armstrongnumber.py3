class ArmstrongNumbers:
    """ Solves the sum of digits challenge. See 
    https://www.codeeval.com/open_challenges/21/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> an = ArmstrongNumbers()
        >>> digits = an.readinput('input.txt')
        >>> len(digits)
        3
        >>> digits[0]
        6
        >>> digits[1]
        153
        >>> digits[2]
        351
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = int(line)
                result.append(line)  
        return result
    
    def isarmstrong(self, number):
        """ Checks if a number is a Armstrong Number.

        Test:
        >>> an = ArmstrongNumbers()
        >>> an.isarmstrong(6)
        True
        >>> an.isarmstrong(153)
        True
        >>> an.isarmstrong(351)
        False
        """
        original = number
        digits = []
        while number:
            number, remainder = divmod(number, 10)
            digits.append(remainder)
        sum = 0
        length = len(digits)
        for digit in digits:
            sum += digit ** length
        return sum == original
        
    def isarmstrongall(self, number_list):
        """ Checks every number if it's a armstrong number.
        
        Test:
        >>> an = ArmstrongNumbers()
        >>> an.isarmstrongall([6, 153, 351])
        [True, True, False]
        """
        result = []
        for number in number_list:
            result.append(self.isarmstrong(number))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        an = ArmstrongNumbers()
        number_list = an.readinput(sys.argv[1])
        result = an.isarmstrongall(number_list)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()