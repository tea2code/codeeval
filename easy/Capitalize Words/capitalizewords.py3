class CapitalizeWords:
    """ Solves the capitalize words challenge. See https://www.codeeval.com/open_challenges/93/ 
    
    Constants:
    DELIMITER -- Input delimiter (string).
    """
    
    DELIMITER = ' '
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> cw = CapitalizeWords()
        >>> lines = cw.readinput('input.txt')
        >>> len(lines)
        4
        >>> lines[0]
        'Hello world'
        >>> lines[1]
        'javaScript language'
        >>> lines[2]
        'a letter'
        >>> lines[3]
        '1st thing'
        """
        lines = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                lines.append(line)
        return lines

    def capitalize(self, text):
        """ Capitalize words.
        
        >>> cw = CapitalizeWords()
        >>> cw.capitalize('Hello world')
        'Hello World'
        """
        return self.DELIMITER.join(w[0].capitalize() + w[1:] for w in text.split(self.DELIMITER)) 
        
    def capitalizeall(self, lines):
        """ Capitalize all words.
        
        Test:
        >>> cw = CapitalizeWords()
        >>> cw.capitalizeall(['Hello world', '1st thing'])
        ['Hello World', '1st Thing']
        """
        result = []
        for text in lines:
            result.append(self.capitalize(text))
        return result
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        cw = CapitalizeWords()
        lines = cw.readinput(sys.argv[1])
        results = cw.capitalizeall(lines)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()