class UniqueElements:
    """ Solves the unique elements challenge. See 
    https://www.codeeval.com/open_challenges/29/ for more information. 
    
    Constants:
    DELIMITER -- The input and output delimiter of values (string).
    """

    DELIMITER = ','
    
    def prettyprint(self, solution):
        """ Prints a solution.
        
        Test:
        >>> ue = UniqueElements()
        >>> ue.prettyprint([{1, 2, 3, 4}, {2, 3, 4, 5}])
        1,2,3,4
        2,3,4,5
        """
        for numbers in solution:
            str_numbers = map(str, numbers)
            print(self.DELIMITER.join(str_numbers))

    def readinput(self, file_name):
        """ Read the input file. Removes duplicates and sorts results.

        Test:
        >>> ue = UniqueElements()
        >>> result = ue.readinput('input.txt')
        >>> len(result)
        3
        >>> result[0]
        [1, 2, 3, 4]
        >>> result[1]
        [2, 3, 4, 5]
        >>> result[2]
        [2, 3, 4, 5]
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                numbers = map(int, line.split(self.DELIMITER))
                numbers = list(set(numbers))
                numbers.sort()
                result.append(numbers) 
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        ue = UniqueElements()
        result = ue.readinput(sys.argv[1])
        ue.prettyprint(result)
    else:
        import doctest
        doctest.testmod()