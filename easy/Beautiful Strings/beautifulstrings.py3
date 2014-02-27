import re

class BeautifulStrings:
    """ Solves the beautiful strings challenge. 
    See https://www.codeeval.com/open_challenges/83/ 
    """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> bs = BeautifulStrings()
        >>> strings = bs.readinput('input.txt')
        >>> len(strings)
        5
        >>> strings[0]
        'ABbCcc'
        >>> strings[1]
        'Good luck in the Facebook Hacker Cup this year!'
        >>> strings[2]
        'Ignore punctuation, please :)'
        >>> strings[3]
        'Sometimes test cases are hard to make up.'
        >>> strings[4]
        'So I just go consult Professor Dalves'
        """
        strings = []
        with open(file_name) as file:
            for line in file.readlines():
                strings.append(line.strip())
        return strings

    def beauty(self, string):
        """ Calculates the beauty of a string.
        
        >>> bs = BeautifulStrings()
        >>> bs.beauty('ABbCcc')
        152
        >>> bs.beauty('Good luck in the Facebook Hacker Cup this year!')
        754
        """
        # Remove non alpha and convert to lower.
        string = string.lower()
        string = re.sub(r'[^a-z]+', '', string)
        
        # Collect every character.
        characters = {}
        for char in string:
            value = characters.setdefault(char, 0)
            value += 1
            characters[char] = value
        
        # Add value to characters and sum up.
        occurrences = list(characters.values())
        occurrences.sort(reverse=True)
        multi = 26
        result = 0
        for num in occurrences:
            result += num * multi
            multi -= 1
        return result
        
    def beautyall(self, strings):
        """ Calculates the beauty of all strings.
        
        Test:
        >>> bs = BeautifulStrings()
        >>> bs.beautyall(['Ignore punctuation, please :)', 'Sometimes test cases are hard to make up.'])
        [491, 729]
        """
        results = []
        for string in strings:
            results.append(self.beauty(string))
        return results
                
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        bs = BeautifulStrings()
        strings = bs.readinput(sys.argv[1])
        results = bs.beautyall(strings)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()