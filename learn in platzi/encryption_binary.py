KEYS = {
    
    'A':   '01000001',
    'B':   '01000010',
    'C':   '01000011',
    'D':   '01000100',
    'E':   '01000101',
    'F':   '01000110',
    'G':   '01000111',
    'H':   '01001000',
    'I':   '01001001',
    'J':   '01001010',
    'K':   '01001011',
    'L':   '01001100',
    'M':   '01001101',
    'N':   '01001110',
    'O':   '01001111',
    'P':   '01010000',
    'Q':   '01010001',
    'R':   '01010010',
    'S':   '01010011',
    'T':   '01010100',
    'U':   '01010101',
    'V':   '01010110',
    'W':   '01010111',
    'X':   '01011000',
    'Y':   '01011001',
    'Z':   '01011010',
    'a':   '01100001',
    'b':   '01100010',
    'c':   '01100011',
    'd':   '01100100',
    'e':   '01100101',
    'f':   '01100110',
    'g':   '01100111',
    'h':   '01101000',
    'i':   '01101001',
    'j':   '01101010',
    'k':   '01101011',
    'l':   '01101100',
    'm':   '01101101',
    'n':   '01101110',
    'o':   '01101111',
    'p':   '01110000',
    'q':   '01110001',
    'r':   '01110010',
    's':   '01110011',
    't':   '01110100',
    'u':   '01110101',
    'v':   '01110110',
    'w':   '01110111',
    'x':   '01111000',
    'y':   '01111001',
    'z':   '01111010',
    '0':   '00000000',
    '1':   '00000001',
    '2':   '00000010',
    '3':   '00000011',
    '4':   '00000100',
    '5':   '00000101',
    '6':   '00000110',
    '7':   '00000111',
    '8':   '00001000',
    '9':   '00001001',
    ' ':   '10000000',#El scope binrio lo invente =) 
}

def encrypt():
    words_to_encrypt = input('Digite una frase a encryptar: ')
    words_encrypted = []

    for character in words_to_encrypt:
        for key,value in KEYS.items():
            if key == character:
                words_encrypted.append(value)


    words_encrypted = ''.join(words_encrypted)
    print('su palabra encriptada es: ', words_encrypted)


def decrypt():
    words_to_decrypt = input('Digite una secuenia binaria a desencriptar: ')
    list_of_encrypted_words = []

    for bit in range(len(words_to_decrypt)//8):
        list_of_encrypted_words.append(words_to_decrypt[(bit*8):((bit*8)+8)])

    for byte in range(len(list_of_encrypted_words)):
        for key,value in KEYS.items():
            if list_of_encrypted_words[byte] == value:
                print(key, end='')
    print('')







if __name__ == '__main__':
   

    while True:
        print('''           
------------------------------------------------------
|            ENCRIPTA TU MENSAJE                     |
|                                                    |
|        Para encriptar presiona [c]                 |
|        para desencriptar presiona [d]              |
|        para salir dale [x]                         |
|                                                    |
------------------------------------------------------
            ''')

        option =  str(input(' ')).lower()

        if option == 'c':
            encrypt()

        if option == 'd':
            decrypt()

        if option == 'x':
            print('SALIR')
            break