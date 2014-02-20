""" Solves the file size challenge. See https://www.codeeval.com/open_challenges/26/ """

import os
import sys
if len(sys.argv) == 2:
    file = sys.argv[1]
    print(os.stat(file).st_size)
else:
    print('Missing argument. Please provide a path to a file.')