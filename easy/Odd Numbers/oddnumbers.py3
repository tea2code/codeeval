def odd_numbers(start, end):
    """ prints the odd numbers in given range.
    
    Test:
    >>> odd_numbers(1, 3)
    1
    3
    >>> odd_numbers(6, 12)
    7
    9
    11
    """
    for i in range(start, end + 1):
        if i % 2:
            print(i)
        
if __name__ == '__main__':
    odd_numbers(1, 99)
    #import doctest
    #doctest.testmod()