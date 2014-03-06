class SwapCase:
    """ Solves the swap case challenge. See https://www.codeeval.com/open_challenges/96/ 
    
    Constants:
    DELIMITER -- Input delimiter (string).
    """
    
    DELIMITER = ' '
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> sc = SwapCase()
        >>> lines = sc.readinput('input.txt')
        >>> len(lines)
        3
        >>> lines[0]
        'Hello world!'
        >>> lines[1]
        'JavaScript language 1.8'
        >>> lines[2]
        'A letter'
        """
        lines = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                lines.append(line)
        return lines

    def swapcase(self, text):
        """ Swap case of words.
        
        >>> sc = SwapCase()
        >>> sc.swapcase('Hello world!')
        'hELLO WORLD!'
        """
        return text.swapcase()
        
    def swapcaseall(self, lines):
        """ Swap case all words.
        
        Test:
        >>> sc = SwapCase()
        >>> sc.swapcaseall(['JavaScript language 1.8', 'A letter'])
        ['jAVAsCRIPT LANGUAGE 1.8', 'a LETTER']
        """
        result = []
        for text in lines:
            result.append(self.swapcase(text))
        return result
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        sc = SwapCase()
        lines = sc.readinput(sys.argv[1])
        results = sc.swapcaseall(lines)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()