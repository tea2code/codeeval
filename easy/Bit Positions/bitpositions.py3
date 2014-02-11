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
        
class BitPosition:
    """ Solves the Bit Position challenge. See https://www.codeeval.com/browse/19/ 
    
    Constants:
    DELIMITER -- The input delimiter of values (string).
    """
    
    DELIMITER = ','
    
    def prettyprint(self, issame):
        """ Prints list of boolean to lowercase.
        
        Test:
        >>> bp = BitPosition()
        >>> bp.prettyprint([True, False])
        true
        false
        """
        for bool in issame:
            if bool:
                print('true')
            else:
                print('false')
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> bp = BitPosition()
        >>> param = bp.readinput('input.txt')
        >>> param[0]
        (86, 2, 3)
        >>> param[1]
        (125, 1, 2)
        """
        param = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                line_param = map(int, line.split(self.DELIMITER))
                param.append(tuple(line_param))
        return param
        
    def issame(self, number, pos1, pos2):
        """ Checks if the bits at both positions are the same in number.
        Positions are 1 based. 
        
        Test:
        >>> bp = BitPosition()
        >>> bp.issame(86, 2, 3)
        True
        >>> bp.issame(125, 1, 2)
        False
        """
        bit1 = Bit.get_bit(number, pos1 - 1)
        bit2 = Bit.get_bit(number, pos2 - 1)
        return bit1 == bit2
        
    def issameall(self, params):
        """ Executes is_same() on list of parameter. 
        
        Test:
        >>> bp = BitPosition()
        >>> bp.issameall([(86, 2, 3), (125, 1, 2)])
        [True, False]
        """
        result = []
        for param in params:
            result.append(self.issame(param[0], param[1], param[2]))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        bp = BitPosition()
        param = bp.readinput(sys.argv[1])
        issame = bp.issameall(param)
        bp.prettyprint(issame)
    else:
        import doctest
        doctest.testmod()