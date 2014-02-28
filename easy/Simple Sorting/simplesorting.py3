class SimpleSorting:
    """ Solves the simple sorting challenge. See https://www.codeeval.com/open_challenges/91/ 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    """
    
    DELIMITER = ' '
    
    def prettyprint(self, numbers):
        """ Prints the result.
        
        Test:
        >>> ss = SimpleSorting()
        >>> ss.prettyprint([['4.6', '3.8', '5.9'], ['-1.083', '382.939']])
        4.6 3.8 5.9
        -1.083 382.939
        """
        for line in numbers:
            line = self.DELIMITER.join(line)
            print(line)
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> ss = SimpleSorting()
        >>> numbers = ss.readinput('input.txt')
        >>> len(numbers)
        2
        >>> numbers[0]
        ['70.920', '-38.797', '14.354', '99.323', '90.374', '7.581']
        >>> numbers[1]
        ['-37.507', '-3.263', '40.079', '27.999', '65.213', '-55.552']
        """
        numbers = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                string_numbers = line.split(self.DELIMITER)
                numbers.append(string_numbers)
        return numbers

    def sort(self, numbers):
        """ Sort numbers.
        
        >>> ss = SimpleSorting()
        >>> ss.sort(['70.920', '-38.797', '14.354', '99.323', '90.374', '7.581'])
        ['-38.797', '7.581', '14.354', '70.920', '90.374', '99.323']
        """
        numbers.sort(key=float)
        return numbers
        
    def sortall(self, numbers):
        """ Reverse every word tuple in the given list. 
        
        Test:
        >>> ss = SimpleSorting()
        >>> ss.sortall([['70.920', '-38.797', '14.354', '99.323', '90.374', '7.581'], ['-37.507', '-3.263', '40.079', '27.999', '65.213', '-55.552']])
        [['-38.797', '7.581', '14.354', '70.920', '90.374', '99.323'], ['-55.552', '-37.507', '-3.263', '27.999', '40.079', '65.213']]
        """
        result = []
        for line_numbers in numbers:
            result.append(self.sort(line_numbers))
        return result
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        ss = SimpleSorting()
        numbers = ss.readinput(sys.argv[1])
        result = ss.sortall(numbers)
        ss.prettyprint(result)
    else:
        import doctest
        doctest.testmod()