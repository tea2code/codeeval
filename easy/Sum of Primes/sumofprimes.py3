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
        
def sum_primes(number):
    """ Calculates the sum of the first x primes. See https://www.codeeval.com/open_challenges/4/
    
    Test:
    >>> sum_primes(3)
    10
    >>> sum_primes(5)
    28
    >>> sum_primes(1000)
    3682913
    """
    current = 2
    count = 0
    sum_primes = 0
    while(count < number):
        if Prime.is_prime(current):
            count += 1
            sum_primes += current
        current += 1
    return sum_primes
        
if __name__ == '__main__':
    print(sum_primes(1000))
    #import doctest
    #doctest.testmod()