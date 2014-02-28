class LongestLines:
    """ Solves the longest lines challenge. See https://www.codeeval.com/open_challenges/2/ """
    
    def readinput(self, file_name):
        """ Read the input file. Returns the number of longest lines as first 
        result and the list of lines as second.

        Test:
        >>> ll = LongestLines()
        >>> num, lines = ll.readinput('input.txt')
        >>> num
        2
        >>> len(lines)
        5
        >>> lines[0]
        'Hello World'
        >>> lines[1]
        'CodeEval'
        >>> lines[2]
        'Quick Fox'
        >>> lines[3]
        'A'
        >>> lines[4]
        'San Francisco'
        """
        lines = []
        with open(file_name) as file:
            for line in file.readlines():
                lines.append(line.strip())
        return int(lines[0]), lines[1:]

    def longestlines(self, num, lines):
        """ Reverse given words. 
        
        >>> ll = LongestLines()
        >>> ll.longestlines(2, ['ab', 'abc', 'a'])
        ['abc', 'ab']
        """
        lines.sort(key=len, reverse=True)
        return lines[:num]
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        ll = LongestLines()
        num, lines = ll.readinput(sys.argv[1])
        results = ll.longestlines(num, lines)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()