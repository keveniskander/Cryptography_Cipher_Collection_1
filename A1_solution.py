"""
-----------------------------
CP460 (Fall 2020)
Name: Keven Iskander
ID:   160634540
Assignment 1
-----------------------------
"""
import utilities
import math

dict_file = 'engmix.txt'

"""
----------------------------------------------------
            Task 1: Plaintext Detection
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   dict_file (str): filename
Return:       dict_list (list): 2D list
Description:  Reads a given dictionary file
              dictionary is assumed to be formatted: each word in a separate line
              Returns a list of lists, list 0 contains all words starting with 'a'
              list 1 all words starting with 'b' and so forth.
Asserts:      dict_file is a non-empty string
---------------------------------------------------
"""
def load_dictionary(dict_file):
    
    assert type(dict_file) == str, 'invalid dict_file'
    assert len(dict_file) > 0, 'invalid dict_file'

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dict_list = [[] for i in range(len(alpha))]

    # print(dict_list)
    file1 = open(dict_file, encoding="ISO-8859-15")
    # a = len(alpha) 
    line = file1.readline() 

    while line:

        line = line.strip()
        b = alpha.find(line[0])
        dict_list[b].append(line)

        line = file1.readline()
        

    return dict_list

"""
----------------------------------------------------
Parameters:   text (str)
Return:       word_list (list)
Description:  Reads a given text
              Returns a list of strings, each pertaining to a word in file
              Words are separated by a white space (space, tab or newline)
              Gets rid of all special characters at the start and at the end
Asserts:      text is a string
---------------------------------------------------
"""
def text_to_words(text):

    assert type(text) == str, 'invalid text'

    special_char = utilities.get_base('special')
    word_list = text.split()
    for a in range(len(word_list)):

        if len(word_list[a])>1:
            word_list[a] = word_list[a].rstrip(special_char)
            word_list[a] = word_list[a].lstrip(special_char)

        if word_list[a] == '':
            word_list[a] = ' '

    return word_list

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str)
Return:       match (int)
              mismatch (int)
Description:  Reads a given text, checks if each word appears in given dictionary
              Returns number of matches and number of mismatches.
              Words are compared in lowercase
              Uses load_dictionary and text_to_words functions
Asserts:      text and dict_file are both strings
---------------------------------------------------
"""
def analyze_text(text, dict_file):

    assert type(text) == str, 'invalid text'
    assert type(dict_file) == str, 'invalid dict_file'
    
    dict_list = load_dictionary(dict_file)
    word_list = text_to_words(text)
    match = 0
    mismatch = 0
    letter = ''
    # print(word_list)
    # print(len(dict_list[0]))
    for i in range(len(word_list)):
        # print(word_list[i])
        letter = word_list[i][0]
        letter = letter.lower()
        # print(letter)
        number = ord(letter) - 97
        # print(number)
        # print(letter)
        if number>=0:

            for j in range(len(dict_list[number])):
                if dict_list[number][j] == word_list[i].lower():
                    match+=1
                    
        

    mismatch = len(word_list)-match
    return match,mismatch

"""
----------------------------------------------------
Parameters:   text (str)
              dict_file (str): dictionary file
              threshold (float): number between 0 to 1
Return:       True/False
Description:  Check if a given file is a plaintext
              If #matches/#words >= threshold --> True
                  otherwise --> False
              If invalid threshold or not given, default is 0.9
              An empty string should return False
---------------------------------------------------
"""
def is_plaintext(text, dict_file, threshold=0.9):

    match, _ = analyze_text(text, dict_file)
    word_list = text_to_words(text)
    # print(match/len(word_list))
    if match/len(word_list) >= threshold and text.strip():
        return True

    return False

"""
----------------------------------------------------
            Task 2: Extended Atbash Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:     plaintext(str)
                key (int)
Return:         ciphertext (str)
Description:    Encryption using Atbash Cipher
                If key = 0, uses lower case base
                If key = 1, uses upper case base
                If key = 2: uses upper+lower case
                If key = 3: uses upper+lower+num
                If key = 4: uses upper+lower+num+special
Asserts:      plaintext is a string and key is an integer
---------------------------------------------------
"""
def e_eatbash(plaintext, key):
    
    assert type(plaintext) == str, 'invalid plaintext'
    assert type(key) == int, "invalid key"

    # alphabet = utilities.get_base('lower')
    ciphertext = ''
    # word_list = text_to_words(plaintext)
    # print(alphabet)

    if key < 0 or key > 4:
        key = key % 5

    if key == 0:
        alphabet = utilities.get_base('lower')
    elif key == 1:
        alphabet = utilities.get_base('upper')
    elif key == 2:
        alphabet = utilities.get_base('alpha')
    elif key == 3:
        alphabet = utilities.get_base('alphanum')
    elif key == 4:
        alphabet = utilities.get_base('all')
        
    for i in range(len(plaintext)):

        if plaintext[i] in alphabet and (key == 0 or key == 1):
            ciphertext += alphabet[25-alphabet.index(plaintext[i])]

        elif plaintext[i] in alphabet and (key == 2):
            ciphertext += alphabet[51-alphabet.index(plaintext[i])]

        elif plaintext[i] in alphabet and (key == 3):
            ciphertext += alphabet[61-alphabet.index(plaintext[i])]

        elif plaintext[i] in alphabet and (key == 4):
            ciphertext += alphabet[93-alphabet.index(plaintext[i])]
            
        else:
            ciphertext += plaintext[i]

    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (int)
Return:       plaintext (str)
Description:  Decryption using Atbash Cipher
              There is no key (None)
              Decryption can be achieved by encrypting ciphertext!!
Asserts:      ciphertext is a string and key is an integer
----------------------------------------------------
"""
def d_eatbash(ciphertext, key):

    assert type(ciphertext) == str
    
    plaintext = e_eatbash(ciphertext, key)

    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
Return:       key (str)
              plaintext (str)
Description:  Cryptanalysis of Extended Atbash Cipher
              Key is in the range of 0-4
              Uses default dictionary file and threshold of 0.8
Asserts:      ciphertext is a string
----------------------------------------------------
"""
def cryptanalysis_eatbash(ciphertext):

    assert type(ciphertext) == str, 'invalid ciphertext'
    
    if is_plaintext(d_eatbash(ciphertext, key=0), dict_file, threshold=0.8) == True:
        return 0, d_eatbash(ciphertext, key=0)

    elif is_plaintext(d_eatbash(ciphertext, key=1), dict_file, threshold=0.8) == True:
        return 1, d_eatbash(ciphertext, key=1)

    elif is_plaintext(d_eatbash(ciphertext, key=2), dict_file, threshold=0.8) == True:
        return 2, d_eatbash(ciphertext, key=2)

    elif is_plaintext(d_eatbash(ciphertext, key=3), dict_file, threshold=0.8) == True:
        return 3, d_eatbash(ciphertext, key=3)

    elif is_plaintext(d_eatbash(ciphertext, key=4), dict_file, threshold=0.8) == True:
        return 4, d_eatbash(ciphertext, key=4)

    else:
        return None,''

"""
----------------------------------------------------
            Task 3: Scytale Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   plaintext(str)
              key (int)
Return:       ciphertext (string)
Description:  Encryption using Scytale Cipher
              Key is the diameter, i.e. # rows
              Assume infinite length rod (infinite #columns)
Asserts:      plaintext is a string
              key is a positive integer
---------------------------------------------------
"""
def e_scytale(plaintext, key):

    assert type(plaintext) == str, 'invalid plaintext'
    assert type(key) == int, 'invalid key'
    assert key > 0, 'invalid key'
   
    col = int(math.ceil(len(plaintext)/key))
    text_matrix = utilities.new_matrix(key, col, '')
    count = 0
    ciphertext = ''

    # print(key, col)
    for i in range(key):
        for j in range(col):
            # utilities.print_matrix(text_matrix)
            if count < len(plaintext):
                text_matrix[i][j] = plaintext[count]
            count +=1

    # utilities.print_matrix(text_matrix)

    for k in range(col):
        for l in range(key):
            ciphertext += text_matrix[l][k]
    

    return ciphertext

"""
----------------------------------------------------
Parameters:   ciphertext(str)
              key (int)
Return:       plaintext (string)
Description:  Decryption using Scytale Cipher
Asserts:      ciphertext is a string
              key is a positive integer
---------------------------------------------------
"""
def d_scytale(ciphertext, key):
    
    assert type(ciphertext) == str, 'invalid ciphertext'
    assert type(key) == int, 'invalid key'
    assert key > 0, 'invalid key'

    col = int(math.ceil(len(ciphertext)/key))
    text_matrix = utilities.new_matrix(key, col, '')
    count = 0
    plaintext = ''
    unused = (key * col) - len(ciphertext) -1

    # utilities.print_matrix(text_matrix)   

    for i in range(col):
        for j in range(key):
            if j == (key-1) and i == (col-1)-unused:
                
                unused-=1
            else:
        
                if count < len(ciphertext):
                    text_matrix[j][i] = ciphertext[count]
                    
                count +=1
    # print(ciphertext)
    # utilities.print_matrix(text_matrix)

    for k in range(key):
        for l in range(col):
            plaintext += text_matrix[k][l]
            

    # print(len(ciphertext), len(plaintext))

    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
Return:       key (int)
              plaintext (str)
Description:  Apply brute-force to break scytale cipher
              Bruteforce range from 1 to 100
Asserts:      ciphertext is a string
---------------------------------------------------
"""
def cryptanalysis_scytale(ciphertext):
    
    assert type(ciphertext) == str, 'invalid ciphertext'

    for i in range(1,100):
        text = d_scytale(ciphertext, i)
        if is_plaintext(text, dict_file, threshold=0.9) == True:
            return i, text

    return None,''

"""
----------------------------------------------------
            Task 4: Polybius Cipher
----------------------------------------------------
"""

"""
----------------------------------------------------
Parameters:   start (str): an ASCII character
              size (int) number of rows & columns in square
Return:       square (str): A string representing a Polybius square
Description:  Creates a string that begins with 'start' character and 
              contains consecutive ASCII characters that are good to fill
              the given size of a polybius square
Asserts:      start is a single character string
              size is an integer >= 2
---------------------------------------------------
"""
def get_polybius_square(start,size):
    
    assert type(start) == str, 'invalid start'
    assert len(start) == 1, 'invalid start'
    assert type(size) == int, 'invalid size'
    assert size >= 2, 'invalid size'

    polybius_square = ''

    # print(polybius_square)
    # print(utilities.get_base('special'))


    total_size = size * size

    try:
        if total_size + ord(start)<126:
            for i in range(ord(start),total_size + ord(start)):
                polybius_square+=chr(i)
        else:
            polybius_square = ''
    except:
        'Error(e_polybius): invalid polybius square'

    return polybius_square

"""--------------------------------------------------------------
Parameters:   plaintext (str)
              key (tuple(str,int))
Return:       ciphertext (str)
Description:  Encryption using Polybius Square
Asserts:      plaintext is a string
              key is a tuple containing a single character and an integer
--------------------------------------------------------------
"""
def e_polybius(plaintext, key):
    
    assert type(plaintext) == str
    assert type(key) == tuple
    assert type(key[0]) == str
    assert len(key[0]) == 1
    assert type(key[1]) == int

    ciphertext = ''
    polybius = get_polybius_square(key[0], key[1])
    total_size = key[1]

    a = 1
    b = 1

    for i in range(len(plaintext)):
        for j in range(len(get_polybius_square(key[0], key[1]))):
            if polybius[j] == plaintext[i]:
                ciphertext += str(a) + str(b)
    
            b += 1
            if b == total_size + 1:
                b = 1
                a += 1
            if a == total_size + 1:
                a = 1
        if plaintext[i] not in polybius:
            ciphertext += plaintext[i]
 

    return ciphertext

"""
-------------------------------------------------------
Parameters:   ciphertext(str)
              key (tuple(str,int))
Return:       plaintext (str)
Description:  Decryption using Polybius Square
Asserts:      ciphertext is a string
              key is a tuple containing a single character and an integer
-------------------------------------------------------
"""
def d_polybius(ciphertext, key):
    
    assert type(ciphertext) == str
    assert type(key) == tuple
    assert type(key[0]) == str
    assert len(key[0]) == 1
    assert type(key[1]) == int

    plaintext = ''
    polybius = get_polybius_square(key[0],key[1])
    total_size = key[1]

    a = 1
    b = 1

    i = 0

    while i < len(ciphertext):
        for j in range(len(get_polybius_square(key[0], key[1]))):
            if (i+1)<len(ciphertext):
                if ciphertext[i] == str(a) and ciphertext[i+1] == str(b):
                    plaintext+=polybius[j]
                    i+=2
                
                # print(str(a), str(b))

            b += 1
            if b == total_size + 1:
                b = 1
                a += 1
            if a == total_size + 1:
                a = 1
        if i < len(ciphertext) and ciphertext[i].isdigit() == False:
            plaintext+=ciphertext[i]
            i +=1
    

    return plaintext

"""
----------------------------------------------------
Parameters:   ciphertext (str)
              size (int)
Return:       key (str)
              plaintext (str)
Description:  Apply brute-force to break polybius cipher
              The size of the polybius square is given
              The square is always located between [' ', '~'] ASCII characters
              Use threshold of 0.93
Asserts:      ciphertext is a string
              size is an integer
---------------------------------------------------
"""
def cryptanalysis_polybius(ciphertext,size):
    # your code here
    return None,''