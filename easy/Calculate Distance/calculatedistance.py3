import re
from math import sqrt

class Point:
    """ Simple representation of a 2D point. 
    
    Member:
    x -- The x coordinate (int).
    y -- The y coordinate (int).
    """
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __str__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

class CalculateDistance:
    """ Solves the Calculate Distance challenge. See 
    https://www.codeeval.com/open_challenges/99/ for more information. """

    def readinput(self, file_name):
        """ Read the input file.

        Test:
        >>> cd =  CalculateDistance()
        >>> points_list = cd.readinput('input.txt')
        >>> len(points_list)
        2
        >>> points_list[0] == (Point(25, 4), Point(1, -6))
        True
        >>> points_list[1] == (Point(47, 43), Point(-25, -11))
        True
        """
        result = []
        with open(file_name) as file:
            for line in file.readlines():
                line = line.strip()
                if not line:
                    continue
                matches = re.search(r'\(\s*([\d-]+)\s*,\s*([\d-]+)\s*\)\s*\(\s*([\d-]+)\s*,\s*([\d-]+)\s*\)', line)
                point_a = Point(int(matches.group(1)), int(matches.group(2)))
                point_b = Point(int(matches.group(3)), int(matches.group(4)))
                result.append((point_a, point_b))
        return result
    
    def distance(self, point_a, point_b):
        """ Calculate distance between both points.

        Test:
        >>> cd =  CalculateDistance()
        >>> cd.distance(Point(25, 4), Point(1, -6))
        26
        >>> cd.distance(Point(47, 43), Point(-25, -11))
        90
        """
        return int(sqrt((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2))
        
    def distanceall(self, points_list):
        """ Calculate distance of all point pairs.
        
        Test:
        >>> cd =  CalculateDistance()
        >>> cd.distanceall([(Point(25, 4), Point(1, -6)), (Point(47, 43), Point(-25, -11))])
        [26, 90]
        """
        result = []
        for pair in points_list:
            result.append(self.distance(pair[0], pair[1]))
        return result
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        cd =  CalculateDistance()
        points_list = cd.readinput(sys.argv[1])
        result = cd.distanceall(points_list)
        for x in result:
            print(x)
    else:
        import doctest
        doctest.testmod()