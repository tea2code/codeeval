import math

class Prime:
    """ Prime number related functions. """
    
    @staticmethod
    def find_primes(number):
        """ Find all prime numbers up to given number. 
        
        Test:
        >>> Prime.find_primes(5)
        [2, 3, 5]
        >>> Prime.find_primes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        """
        all_numbers = list(range(2, number + 1))
        for i, x in enumerate(all_numbers):
            comp = []
            for y in range(i, len(all_numbers)):
                q = x * all_numbers[y]
                if q <= max(all_numbers):
                    comp.append(q)
                else:
                    break
            for z in comp:
                all_numbers.remove(z)
        return all_numbers
    
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
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()