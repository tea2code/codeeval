class FindAWriter:
    """ Solves the find a writer challenge. See 
    https://www.codeeval.com/open_challenges/97/ for more information. 
    
    Constants:
    DELIMITER_PARTS -- The input delimiter of both parts (string).
    DELIMITER_POSITIONS -- The input delimiter of positions (string).
    """

    DELIMITER_PARTS = '|'
    DELIMITER_POSITIONS = ' '
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> fw = FindAWriter()
        >>> result = fw.readinput('input.txt')
        >>> len(result)
        2
        >>> result[0]
        ('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg', [3, 35, 27, 62, 51, 27, 46, 57, 26, 10, 46, 63, 57, 45, 15, 43, 53])
        >>> result[1]
        ('3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA', [2, 26, 33, 55, 34, 50, 33, 61, 44, 28, 46, 32, 28, 30, 3, 50, 34, 61, 40, 7, 1, 31])
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                if not line.strip():
                    continue
                parts = line.split(self.DELIMITER_PARTS)
                numbers = map(int, parts[1].strip().split(self.DELIMITER_POSITIONS))
                result.append((parts[0], list(numbers)))
        return result
        
    def findwriter(self, text, numbers):
        """ Find writer name in text using numbers.
        
        Test:
        >>> fw = FindAWriter()
        >>> fw.findwriter('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg', [3, 35, 27, 62, 51, 27, 46, 57, 26, 10, 46, 63, 57, 45, 15, 43, 53])
        'Stephen King 1947'
        >>> fw.findwriter('3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA', [2, 26, 33, 55, 34, 50, 33, 61, 44, 28, 46, 32, 28, 30, 3, 50, 34, 61, 40, 7, 1, 31])
        'Kyotaro Nishimura 1930'
        """
        result = ''
        for number in numbers:
            result += text[number - 1]
        return result
        
    def findwriterall(self, params):
        """ Find writer name in text using numbers for all parameter.
        
        Test:
        >>> fw = FindAWriter()
        >>> fw.findwriterall([('osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg', [3, 35, 27, 62, 51, 27, 46, 57, 26, 10, 46, 63, 57, 45, 15, 43, 53])])
        ['Stephen King 1947']
        """
        result = []
        for param in params:
            result.append(self.findwriter(param[0], param[1]))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        fw = FindAWriter()
        params = fw.readinput(sys.argv[1])
        results = fw.findwriterall(params)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()