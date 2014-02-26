class HexToDecimal:
    """ Solves the hex to decimal challenge. 
    See https://www.codeeval.com/browse/67/ """
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> hd = HexToDecimal()
        >>> hex_list = hd.readinput('input.txt')
        >>> len(hex_list)
        2
        >>> hex_list[0]
        '9f'
        >>> hex_list[1]
        '11'
        """
        hex_list = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                hex_list.append(line)
        return hex_list
        
    def dec(self, hex):
        """ Converts hex to dec.
        
        Test:
        >>> hd = HexToDecimal()
        >>> hd.dec('9f')
        159
        >>> hd.dec('11')
        17
        """
        return int(hex, 16)
        
    def decall(self, hex_list):
        """ Executes dec() on list of parameter. 
        
        Test:
        >>> hd = HexToDecimal()
        >>> hd.decall(['9f', '11'])
        [159, 17]
        """
        result = []
        for hex in hex_list:
            result.append(self.dec(hex))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        hd = HexToDecimal()
        hex_list = hd.readinput(sys.argv[1])
        results = hd.decall(hex_list)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()