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
        if plaintext[i] in alphabet:
            ciphertext += alphabet[25-alphabet.index(plaintext[i])]
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
    
    plaintext = ''

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
    
    key = 0
    plaintext = ''

    return key,plaintext

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
   
    ciphertext = ''

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
    
    plaintext = ''

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
    # your code here
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
    
    polybius_square = ''

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
    
    ciphertext = ''

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
    
    plaintext = ''

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