class NModM:
    """ Solves the n mod m challenge. 
    See https://www.codeeval.com/browse/62/ 
    
    Constants:
    DELIMITER -- The input delimiter of values (string).
    """
    
    DELIMITER = ','
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> nm = NModM()
        >>> params = nm.readinput('input.txt')
        >>> len(params)
        2
        >>> params[0]
        (20, 6)
        >>> params[1]
        (2, 3)
        """
        params = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                line_param = map(int, line.split(self.DELIMITER))
                params.append(tuple(line_param))
        return params
        
    def modulo(self, n, m):
        """ Calculates n modulo m.
        First calculates the result of the 
        integer division. Multiplicates this
        result by the divisor and then substractes 
        this from the dividend.
        
        Test:
        >>> nm = NModM()
        >>> nm.modulo(20, 6)
        2
        >>> nm.modulo(2, 3)
        2
        >>> nm.modulo(-5, 3)
        -2
        """
        return n - (int(n/m) * m)
        
    def moduloall(self, params):
        """ Executes modulo() on list of parameter. 
        
        Test:
        >>> nm = NModM()
        >>> nm.moduloall([(20, 6), (2, 3)])
        [2, 2]
        """
        result = []
        for param in params:
            result.append(self.modulo(param[0], param[1]))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        nm = NModM()
        params = nm.readinput(sys.argv[1])
        results = nm.moduloall(params)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()