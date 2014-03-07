class QueryBoard:
    """ Solves the query board challenge. See https://www.codeeval.com/open_challenges/87/ 
    
    Constants:
    COLUMNS -- Number of columns in board (int).
    DEFAULT -- The default value of columns (int).
    DELIMITER -- The input and output delimiter of values (string).
    ROWS -- Number of rows in board (int).
    
    Member:
    board -- A list of rows which are lists of columns (list).
    """
    
    COLUMNS = 256
    DEFAULT = 0
    DELIMITER = ' '
    ROWS = 256
    
    def __init__(self):
        """ Test:
        >>> qb = QueryBoard()
        >>> qb.board[0] == [qb.DEFAULT] * qb.COLUMNS
        True
        >>> len(qb.board)
        256
        """
        self.board = [[self.DEFAULT] * self.COLUMNS for _ in range(self.ROWS)]
    
    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> qb = QueryBoard()
        >>> commands = qb.readinput('input.txt')
        >>> len(commands)
        10
        >>> commands[0]
        ('SetCol', 32, 20)
        >>> commands[1]
        ('SetRow', 15, 7)
        >>> commands[3]
        ('QueryCol', 32)
        """
        commands = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                line_params = line.split(self.DELIMITER)
                command = [line_params[0]] + list(map(int, line_params[1:]))
                commands.append(tuple(command))
        return commands

    def execute(self, command):
        """ Execute given command. A command is a tuple where the 
        first item is the command string and the following values 
        are parameter for this command.
        
        >>> qb = QueryBoard()
        >>> qb.execute(('SetCol', 32, 20))
        >>> qb.board[0][32]
        20
        >>> qb.board[255][32]
        20
        >>> qb.execute(('SetRow', 1, 6))
        >>> qb.board[1] == [6] * qb.COLUMNS
        True
        """
        result = None
        if command[0] == 'SetCol':
            self.setcolumn(command[1], command[2])
        elif command[0] == 'SetRow':
            self.setrow(command[1], command[2])
        elif command[0] == 'QueryCol':
            result = self.querycolumn(command[1])
        elif command[0] == 'QueryRow':
            result = self.queryrow(command[1])
        else:
            raise RuntimeError('Unknown command "{0}".'.format(command[0]))
        return result
        
    def executeall(self, commands):
        """ Execute all commands.
        
        Test:
        >>> qb = QueryBoard()
        >>> qb.executeall([('SetCol', 32, 20), ('SetRow', 15, 7), ('SetRow', 16, 31), ('QueryCol', 32)])
        [5118]
        """
        results = []
        for command in commands:
            result = self.execute(command)
            if result is not None:
                results.append(result)
        return results
        
    def querycolumn(self, j):
        """ Query a column. """
        return sum([self.board[i][j] for i in range(self.ROWS)])
        
    def queryrow(self, i):
        """ Query a row. """
        return sum(self.board[i])
        
    def setcolumn(self, j, x):
        """ Set a column. """
        for i in range(self.ROWS):
            self.board[i][j] = x
        
    def setrow(self, i, x):
        """ Set a row. """
        self.board[i] = [x] * self.COLUMNS
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        qb = QueryBoard()
        commands = qb.readinput(sys.argv[1])
        results = qb.executeall(commands)
        for result in results:
            print(result)
    else:
        import doctest
        doctest.testmod()