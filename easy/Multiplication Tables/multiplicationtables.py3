def print_multiplication_table(x_limit, y_limit, width):
    """ Print the grade school multiplication table 
    up to given limits. Width defines the width of a value.
    Spaces are added if necessary.
    """
    for x in range(1, x_limit + 1):
        line = ''
        for y in range(1, y_limit + 1):
            value = y * x
            line += (str(value).rjust(width))
        # Print line without leading/trailing spaces.
        print(line.strip()) 

if __name__ == '__main__':
    print_multiplication_table(12, 12, 4)