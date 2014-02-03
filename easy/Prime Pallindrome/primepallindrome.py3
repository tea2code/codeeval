import math

class Prime:
    """ Prime number related functions. """
    
    @staticmethod
    def is_prime(number):
        """ Tests if a number is a prime. It uses the fairly fast method of 
        checking up to the square of number while skipping even numbers. 
        See http://stackoverflow.com/a/18833870/1931663 for more information. 
        
        Test:
        >>> Prime.is_prime(2)
        True
        >>> Prime.is_prime(3)
        True
        >>> Prime.is_prime(11)
        True
        >>> Prime.is_prime(4)
        False
        >>> Prime.is_prime(9)
        False
        """
        if number % 2 == 0 and number > 2: 
            return False
        for divisor in range(3, int(math.sqrt(number)) + 1, 2):
            if number % divisor == 0:
                return False
        return True

class PrimePallindrome:
    """ Finds a prime pallindrome. See https://www.codeeval.com/open_challenges/3/ """
    
    @staticmethod
    def find_highest(number):
        """ Find highest prime pallindrome which is equal or smaller the given 
        number. Numbers below 11 are not considered because 11 is the last 
        pallindrome.
        
        Test:
        >>> PrimePallindrome.find_highest(1000)
        929
        >>> PrimePallindrome.find_highest(12)
        11
        >>> PrimePallindrome.find_highest(11)
        11
        """
        assert number >= 11
        for candidate in range(number, 10, -1):
            if PrimePallindrome.is_pallindrome(candidate) and Prime.is_prime(candidate):
                return candidate
        
    @staticmethod
    def is_pallindrome(number):
        """ Check if a number is a pallindrome. The check uses string conversion
        because being a pallindrome is a lexical property not a mathematical.
        
        Test:
        >>> PrimePallindrome.is_pallindrome(929)
        True
        >>> PrimePallindrome.is_pallindrome(11)
        True
        >>> PrimePallindrome.is_pallindrome(12)
        False
        """
        numstring = str(number)
        return numstring == numstring[::-1]
        
if __name__ == '__main__':
    print(PrimePallindrome.find_highest(1000))
    #import doctest
    #doctest.testmod()