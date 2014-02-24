class RightmostChar:
    """ Solves the rightmost char challenge. See https://www.codeeval.com/open_challenges/31/ 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    """
    
    DELIMITER = ','
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> rc = RightmostChar()
        >>> params = rc.readinput('input.txt')
        >>> len(params)
        3
        >>> params[0]
        ('Hello World', 'r')
        >>> params[1]
        ('Hello CodeEval', 'E')
        >>> params[2]
        ('All your base are belong to us', 't')
        """
        params = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                line_params = line.split(self.DELIMITER)
                params.append(tuple(line_params))
        return params

    def rightmost(self, text, char):
        """ Find the rightmost char in text.
        
        >>> rc = RightmostChar()
        >>> rc.rightmost('Hello World', 'r')
        8
        """
        return text.rfind(char)
        
    def rightmostall(self, params):
        """ Find the rightmost char in given list.
        
        Test:
        >>> rc = RightmostChar()
        >>> rc.rightmostall([('Hello World', 'r'), ('Hello CodeEval', 'E')])
        [8, 10]
        """
        result = []
        for text, char in params:
            result.append(self.rightmost(text, char))
        return result
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        rc = RightmostChar()
        params = rc.readinput(sys.argv[1])
        results = rc.rightmostall(params)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()