class MultiplesNumber:
    """ Solves the multiples of a number challenge. See 
    https://www.codeeval.com/open_challenges/18/ for more information. 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    """

    DELIMITER = ','
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> mn = MultiplesNumber()
        >>> params = mn.readinput('input.txt')
        >>> len(params)
        5
        >>> params[0]
        (13, 8)
        >>> params[1]
        (17, 16)
        >>> params[2]
        (13, 2)
        >>> params[3]
        (8, 8)
        >>> params[4]
        (16, 8)
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                xn = map(int, line.split(self.DELIMITER))
                result.append(tuple(xn))  
        return result
    
    def multiple_of(self, x, n):
        """ Find a multiple of n which is greater or equal x. 
        
        Test:
        >>> mn = MultiplesNumber()
        >>> mn.multiple_of(13, 8)
        16
        >>> mn.multiple_of(17,16)
        32
        >>> mn.multiple_of(13, 2)
        14
        >>> mn.multiple_of(8, 8)
        8
        >>> mn.multiple_of(16, 8)
        16
        """
        current_n = n
        step = 2
        while current_n < x:
            current_n = n * step
            step += 1
        return current_n
        
    def multiple_of_all(self, xn_list):
        """ Find multiples of all tuples in list. 
        
        Test:
        >>> mn = MultiplesNumber()
        >>> mn.multiple_of_all([(13, 8), (17, 16), (13, 2), (8, 8), (16, 8)])
        [16, 32, 14, 8, 16]
        """
        result = []
        for xn in xn_list:
            result.append(self.multiple_of(xn[0], xn[1]))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        mn = MultiplesNumber()
        xn_list = mn.readinput(sys.argv[1])
        result = mn.multiple_of_all(xn_list)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()