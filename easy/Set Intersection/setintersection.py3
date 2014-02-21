class SetIntersection:
    """ Solves the set intersection challenge. See 
    https://www.codeeval.com/open_challenges/30/ for more information. 
    
    Constants:
    DELIMITER_INT -- The input and output delimiter of values (string).
    DELIMITER_SET -- The input delimiter of sets (string).
    """

    DELIMITER_INT = ','
    DELIMITER_SET = ';'
    
    def prettyprint(self, solutions):
        """ Prints a solution.
        
        Test:
        >>> se = SetIntersection()
        >>> se.prettyprint([[4], [], [1, 2, 3]])
        4
        <BLANKLINE>
        1,2,3
        """
        for solution in solutions:
            line = self.DELIMITER_INT.join(map(str, solution))
            print(line)

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> se = SetIntersection()
        >>> result = se.readinput('input.txt')
        >>> len(result)
        3
        >>> result[0]
        [[1, 2, 3, 4], [4, 5, 6]]
        >>> result[1]
        [[20, 21, 22], [45, 46, 47]]
        >>> result[2]
        [[7, 8, 9], [8, 9, 10, 11, 12]]
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line_sets = line.split(self.DELIMITER_SET)
                sets = []
                for s in line_sets:
                    numbers = map(int, s.split(self.DELIMITER_INT))
                    sets.append(list(numbers))
                result.append(sets) 
        return result
        
    def intersect(self, sets):
        """ Find intersection of given sets. 
        
        Test:
        >>> se = SetIntersection()
        >>> se.intersect([[1, 2, 3], [2, 3]])
        [2, 3]
        >>> se.intersect([[4, 5], [6, 7, 8]])
        []
        """
        result = list(set(sets[0]).intersection(sets[1]))
        result.sort()
        return result
        
    def intersectall(self, list_sets):
        """ Find intersection of all given list of sets. 
        
        Test:
        >>> se = SetIntersection()
        >>> se.intersectall([[[1, 2, 3], [2, 3]], [[4, 5], [6, 7, 8]]])
        [[2, 3], []]
        """
        result = []
        for sets in list_sets:
            result.append(self.intersect(sets))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        se = SetIntersection()
        sets = se.readinput(sys.argv[1])
        result = se.intersectall(sets)
        se.prettyprint(result)
    else:
        import doctest
        doctest.testmod()