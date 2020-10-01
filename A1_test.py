"""----------------------------------------------------
Task 1: Plaintext Detection
----------------------------------------------------"""
import utilities
import A1_solution

def task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Plaintext Detection Testing")
    print()

    dict_list = A1_solution.load_dictionary("engmix.txt")
    print('Testing load_dictionary:')
    print("Number of words starting with b = ",len(dict_list[1]))
    print("10th word starting with P = ",dict_list[15][9])
    print("100th word starting with j = ",dict_list[9][99])
    print("Last word starting with s = ",dict_list[18][-1])
    print()
    
    print("Testing text_to_words:")
    plaintext1 = utilities.file_to_text("plaintext11.txt")
    word_list = A1_solution.text_to_words(plaintext1)
    print("plaintext1:", word_list)

    plaintext2 = utilities.file_to_text("plaintext12.txt")
    word_list = A1_solution.text_to_words(plaintext2)
    print("plaintext2:")
    print(word_list)

    plaintext3 = utilities.file_to_text("plaintext13.txt")
    word_list = A1_solution.text_to_words(plaintext3)
    print("plaintext3:")
    print(word_list)
    print()

    print("Testing analyze_text:")
    result = A1_solution.analyze_text(plaintext2,"engmix.txt")
    print("Analyzing plaintext2:", result)
    result = A1_solution.analyze_text(plaintext3,"engmix.txt")
    print("Analyzing plaintext3:", result)
    plaintext4 = utilities.file_to_text("plaintext14.txt")
    result = A1_solution.analyze_text(plaintext4,"engmix.txt")
    print("Analyzing plaintext4:", result)
    ciphertext1 = utilities.file_to_text("ciphertext11.txt")
    result = A1_solution.analyze_text(ciphertext1,"engmix.txt")
    print("Analyzing ciphertext1:", result)
    print()
    
    print("Testing is_plaintext:")
    result = A1_solution.is_plaintext(plaintext2,"engmix.txt",0.85)
    print("plaintext2 (0.85):", result)
    result = A1_solution.is_plaintext(plaintext3,"engmix.txt",1.1)
    print("plaintext3 (1.1):", result)
    result = A1_solution.is_plaintext(plaintext3,"engmix.txt",0.96)
    print("plaintext3: (0.96)", result)
    result = A1_solution.is_plaintext(plaintext4,"engmix.txt",0.91)
    print("plaintext4: (0.91)", result)
    result = A1_solution.is_plaintext(plaintext4,"engmix.txt",0.82)
    print("plaintext4: (0.82)", result)
    result = A1_solution.is_plaintext(ciphertext1,"engmix.txt",0.7)
    print("ciphertext1: (0.7)", result)
    print()
    
    print('End of Task 1: Plaintext Detection Testing')
    print('{}'.format('-'*40))
    print()
    return

def task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: Extended Atbash Testing")
    print()
    
    print('-------- Testing Encryption: ')
    plaintext = utilities.file_to_text('plaintext14.txt')
    for i in range(5):
        ciphertext = A1_solution.e_eatbash(plaintext,i+5)
        print('key = {}'.format(i))
        print('ciphertext: ')
        print(ciphertext)
        utilities.text_to_file(ciphertext,'ciphertext2'+str(i+1)+'.txt')
        print()

    print('-------- Testing Decryption: ')
    for i in range(5):
        ciphertext = utilities.file_to_text('ciphertext2'+str(i+1)+'.txt')
        plaintext = A1_solution.d_eatbash(ciphertext,i)
        print('key = {}'.format(i))
        print('plaintext: ')
        print(plaintext)
        print()
    
    print('-------- Testing Cryptanalysis: ')
    for i in range(5):
        file = 'ciphertext2'+str(i+1)+'.txt'
        ciphertext = utilities.file_to_text(file)
        key,plaintext = A1_solution.cryptanalysis_eatbash(ciphertext)
        print('key = {}'.format(key),end=' , ')
        if plaintext == utilities.file_to_text('plaintext14.txt'):
            print('Plaintext verified')
        else:
            print('Plaintext mismatch')
        
    print()
    print('End of Task 2: Extended Atbash Testing')
    print('{}'.format('-'*40))
    print()
    return

def task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Scytale Cipher Testing")
    print()
    
    print('--------- Testing Encryption:')
    for i in range(3,7):
        plainfile = 'plaintext1'+str(i-2)+'.txt'
        plaintext = utilities.file_to_text(plainfile)
        ciphertext = A1_solution.e_scytale(plaintext,i)
        print('key = {}'.format(i))
        print('ciphertext: ')
        print(ciphertext)
        utilities.text_to_file(ciphertext,'ciphertext3'+str(i-2)+'.txt')
        print()

    print('-------- Testing Decryption: ')
    for i in range(3,7):
        ciphertext = utilities.file_to_text('ciphertext3'+str(i-2)+'.txt')
        plaintext = A1_solution.d_scytale(ciphertext,i)
        print('key = {}'.format(i))
        print('plaintext: ')
        print(plaintext)
        print()
        
    print('-------- Testing Cryptanalysis: ')
    for i in range(5,7):
        file = 'ciphertext3'+str(i)+'.txt'
        ciphertext = utilities.file_to_text(file)
        key,plaintext = A1_solution.cryptanalysis_scytale(ciphertext)
        print('key = {}'.format(key),end=' , ')
        if plaintext == utilities.file_to_text('plaintext31.txt'):
            print('Plaintext verified')
        else:
            print('Plaintext mismatch')
    print()
    
    print('End of Task 3: Scytale Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

def task4():
    print('{}'.format('-'*40))
    print("Start of Task 4: Polybius Square Cipher Testing")
    print()
    
    print('-------- Testing get_polybius_square:')
    print('start = "A", size = 5: {}'.format(A1_solution.get_polybius_square('A',5)))
    print('start = "R", size = 6: {}'.format(A1_solution.get_polybius_square('R',6)))
    print('start = "@", size = 7: {}'.format(A1_solution.get_polybius_square('@',7)))
    print('start = "A", size = 5: {}'.format(A1_solution.get_polybius_square('A',5)))
    print('start = " ", size = 8: {}'.format(A1_solution.get_polybius_square(' ',8)))
    print('start = "+", size = 9: {}'.format(A1_solution.get_polybius_square('+',9)))
    print('start = " ", size = 10: {}'.format(A1_solution.get_polybius_square(' ',10)))
    print()
    
    print('-------- Testing Encryption:')
    
    start = ['D','A',' ','+','B']
    for i in range(1,6):
        plainfile = 'plaintext4'+str(i)+'.txt'
        plaintext = utilities.file_to_text(plainfile)
        key = (start[i-1],i+5)
        ciphertext = A1_solution.e_polybius(plaintext,key)
        print('key = {}'.format(key))
        print('ciphertext: ')
        print(ciphertext)
        utilities.text_to_file(ciphertext,'ciphertext4'+str(i)+'.txt')
        print()
    
    print('-------- Testing Decryption: ')
    for i in range(1,6):
        ciphertext = utilities.file_to_text('ciphertext4'+str(i)+'.txt')
        key = (start[i-1],i+5)
        plaintext = A1_solution.d_polybius(ciphertext,key)
        print('key = {}'.format(key))
        print('plaintext: ')
        print(plaintext)
        print()

    print('-------- Testing Cryptanalysis: ')
    size = [6,9,8]
    for i in range(6,9):
        file = 'ciphertext4'+str(i)+'.txt'
        ciphertext = utilities.file_to_text(file)
        key,plaintext = A1_solution.cryptanalysis_polybius(ciphertext,size[i-6])
        print('key = {} --> {}'.format(key,A1_solution.get_polybius_square(key[0],key[1])),end=' , ')
        if plaintext == utilities.file_to_text('plaintext46.txt'):
            print('Plaintext verified')
        else:
            print('Plaintext mismatch')
    print()
    
    print('End of Task 4: Polybius Square Cipher Testing')
    print('{}'.format('-'*40))
    print()
    return

# task1()
task2()
#task3()
#task4()