# -*-                  -*-
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '&',
}

def encrypt():
    words = str(input('Escribe tus palabras a encriptar: '))

    list_of_words = list(words)

    list_of_encrypt_words = []

   
    for letter in list_of_words:       

        for key in KEYS.keys():

            if letter == key:

                #print(letter)
                list_of_encrypt_words.append(KEYS[letter])


    encrypted_words = ''.join(list_of_encrypt_words)
    #print(len(list_of_words))
    print('------------------------------------------------------')
    print(encrypted_words)
    #print(len(encrypted_words))

def decrypt():
    encrypted_words = str(input('Desencriptar: '))

    list_of_encrypted_words = list(encrypted_words)

    list_of_words = []
        
    for character in list_of_encrypted_words:       

        for key, value in KEYS.items():

            if character == value:

                #character =  key
                list_of_words.append(key)

    words = ''.join(list_of_words)

    #print(len(list_of_encrypted_words))
    print('------------------------------------------------------')
    print(words)
    #print(len(words))


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
            


