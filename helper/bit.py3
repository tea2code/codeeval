class Bit:
    """ Bit operation related helper. """
    
    @staticmethod
    def get_bit(byte_value, index):
        """ Retrieves the bit of byte at the given index. 
        See http://stackoverflow.com/questions/2591483/getting-a-specific-bit-value-in-a-byte-string
        for more information.
        
        Test:
        >>> Bit.get_bit(1, 0)
        1
        >>> Bit.get_bit(1, 1)
        0
        >>> Bit.get_bit(3, 0)
        1
        >>> Bit.get_bit(3, 1)
        1
        >>> Bit.get_bit(3, 2)
        0
        >>> Bit.get_bit(3, 3)
        0
        """
        return ((byte_value & (1 << index)) != 0);
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()