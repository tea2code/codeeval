class ReverseWords:
    """ Solves the reverse words challenge. See https://www.codeeval.com/open_challenges/8/ 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    """
    
    DELIMITER = ' '
    
    def __init__(self):
        self.words = []
    
    def prettyprint(self, words):
        """ Prints tuples of words. Can take a single tuple or a list of 
        tuples. 
        
        Test:
        >>> rw = ReverseWords()
        >>> rw.prettyprint([('Hello', 'World'), ('Hello', 'CodeEval')])
        Hello World
        Hello CodeEval
        """
        if words and not isinstance(words[0], tuple):
            words = [words]
        for line_words in words:
            line = self.DELIMITER.join(line_words)
            print(line)
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> rw = ReverseWords()
        >>> words = rw.readinput('input.txt')
        >>> words[0]
        ('Hello', 'World')
        >>> words[1]
        ('Hello', 'CodeEval')
        >>> words[2]
        ('All', 'your', 'base', 'are', 'belong', 'to', 'us')
        """
        words = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                line_words = line.split(self.DELIMITER)
                words.append(tuple(line_words))
        return words

    def reverse(self, words):
        """ Reverse given words. 
        
        >>> rw = ReverseWords()
        >>> rw.reverse(('Hello', 'World'))
        ('World', 'Hello')
        """
        return words[::-1]
        
    def reverseall(self, words):
        """ Reverse every word tuple in the given list. 
        
        Test:
        >>> rw = ReverseWords()
        >>> rw.reverseall([('Hello', 'World'), ('Hello', 'CodeEval')])
        [('World', 'Hello'), ('CodeEval', 'Hello')]
        """
        reversed = []
        for line_words in words:
            reversed.append(self.reverse(line_words))
        return reversed
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        rw = ReverseWords()
        words = rw.readinput(sys.argv[1])
        reversed = rw.reverseall(words)
        rw.prettyprint(reversed)
    else:
        import doctest
        doctest.testmod()