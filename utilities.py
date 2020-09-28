"""
-----------------------------
CP460 (Fall 2020)
Utilities
Supports: Atbash, Scytale
-----------------------------
"""
import string

"""
----------------------------------------------------
Parameters:   base_type (str) 
Return:       result (str)
Description:  Return a base string containing a subset of ASCII charactes
              Defined base types:
              lower: lower case characters
              upper: upper case characters
              alpha: upper and lower case characters
              lowernum: lower case and numerical characters
              uppernum: upper case and numerical characters
              alphanum: upper, lower and numerical characters
              special: punctuations and special characters (no white space)
              all: upper, lower, numerical and special characters
---------------------------------------------------
"""
def get_base(base_type):
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
            
    result = ''
    if base_type == 'lower':
        result = lower
    elif base_type == 'upper':
        result = upper
    elif base_type == 'alpha':
        result = upper + lower
    elif base_type == 'lowernum':
        result = lower + num
    elif base_type == 'uppernum':
        result = upper + num
    elif base_type == 'alphanum':
        result = upper + lower + num
    elif base_type == 'special':
        result = special
    elif base_type == 'all':
        result = upper + lower + num + special
    else:
        print('Error(get_base): undefined base type')
        result = ''
    return result

"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""
def file_to_text(filename):
    infile = open(filename,'r')
    contents = infile.read()
    infile.close()
    return contents

"""
----------------------------------------------------
Parameters:   text (str)
              filename (str)            
Return:       no returns
Description:  Utility function to write any given text to a file
              If file already exist, previous content will be erased
---------------------------------------------------
"""
def text_to_file(text, filename):
    outfile = open(filename,'w')
    outfile.write(text)
    outfile.close()
    return

"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""
def new_matrix(r,c,fill):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[fill] * c for i in range(r)]

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
                items separated by a tab
#               Assumes given parameter is a valid matrix
---------------------------------------------------
"""
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
---------------------------------------------------
"""
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text

"""#----------------------------------------------------
# Parameters:   None
# Return:       polybius_square (string)
# Description:  Returns the following polybius square
#               as a sequential string:
#               [1] [2]  [3] [4] [5] [6] [7] [8]
#           [1]      !    "   #   $   %   &   '
#           [2]  (   )    *   +   '   -   .   /
#           [3]  0   1    2   3   4   5   6   7
#           [4]  8   9    :   ;   <   =   >   ?
#           [5]  @   A    B   C   D   E   F   G
#           [6]  H   I    J   K   L   M   N   O
#           [7]  P   Q    R   S   T   U   V   W
#           [8]  X   Y    Z   [   \   ]   ^   _
#---------------------------------------------------"""
def get_polybius_square():
    polybius_square = ""
    for i in range(32,96):
        polybius_square+=chr(i)
    return polybius_square