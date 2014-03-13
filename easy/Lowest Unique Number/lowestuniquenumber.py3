class LowestUniqueNumber:
    """ Solves the lowest unique number challenge. See 
    https://www.codeeval.com/open_challenges/103/ for more information. 
    
    Constants:
    DELIMITER -- The input delimiter of values (string).
    """

    DELIMITER = ' '
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> lun = LowestUniqueNumber()
        >>> result = lun.readinput('input.txt')
        >>> len(result)
        2
        >>> result[0]
        [3, 3, 9, 1, 6, 5, 8, 1, 5, 3]
        >>> result[1]
        [9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1]
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                guesses = map(int, line.split(self.DELIMITER))
                result.append(list(guesses)) 
        return result
        
    def lowestuniquenumber(self, guesses):
        """ Find the lowest unique number for all guesses.
        
        Test:
        >>> lun = LowestUniqueNumber()
        >>> lun.lowestuniquenumber([3, 3, 9, 1, 6, 5, 8, 1, 5, 3])
        5
        >>> lun.lowestuniquenumber([9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1])
        0
        """
        unique = []
        seen = []
        for guess in guesses:
            if guess in unique:
                unique.remove(guess)
            elif guess not in seen:
                unique.append(guess)
            seen.append(guess)
        unique.sort()
        return guesses.index(unique[0]) + 1 if unique else 0
        
    def lowestuniquenumberall(self, guesseslist):
        """ Find the lowest unique numbers for all guesses.
        
        Test:
        >>> lun = LowestUniqueNumber()
        >>> lun.lowestuniquenumberall([[3, 3, 9, 1, 6, 5, 8, 1, 5, 3], [9, 2, 9, 9, 1, 8, 8, 8, 2, 1, 1]])
        [5, 0]
        """
        result = []
        for guesses in guesseslist:
            result.append(self.lowestuniquenumber(guesses))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        lun = LowestUniqueNumber()
        guesses = lun.readinput(sys.argv[1])
        results = lun.lowestuniquenumberall(guesses)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()