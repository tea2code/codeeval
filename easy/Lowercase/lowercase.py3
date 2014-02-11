class Lowercase:
    """ Solves the lowercase challenge. See https://www.codeeval.com/open_challenges/20/ """
    
    DELIMITER = ' '
    
    def prettyprint(self, lines):
        """ Prints lines.
        
        Test:
        >>> lc = Lowercase()
        >>> lc.prettyprint(['hello world', 'bla'])
        hello world
        bla
        """
        for line in lines:
            print(line)
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> lc = Lowercase()
        >>> lines = lc.readinput('input.txt')
        >>> lines[0]
        'HELLO CODEEVAL'
        >>> lines[1]
        'This is some text'
        >>> lines[2]
        'All your base ARE beLOng TO us'
        """
        lines = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                lines.append(line)
        return lines

    def lowercase(self, text):
        """ Make text lowercase.
        
        >>> lc = Lowercase()
        >>> lc.lowercase('Hello WOrld')
        'hello world'
        """
        return text.lower()
        
    def lowercaseall(self, lines):
        """ Make all lines lowercase.
        
        Test:
        >>> lc = Lowercase()
        >>> lc.lowercaseall(['Hello World', 'BLA'])
        ['hello world', 'bla']
        """
        result = []
        for line in lines:
            result.append(self.lowercase(line))
        return result
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        lc = Lowercase()
        lines = lc.readinput(sys.argv[1])
        lowerlines = lc.lowercaseall(lines)
        lc.prettyprint(lowerlines)
    else:
        import doctest
        doctest.testmod()