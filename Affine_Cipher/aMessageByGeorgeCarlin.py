import cryptomath
import random

SYMBOLS = """ !_ABCDEFGHIJKLMNOPQRSTUVWXYZ """

def getKey(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


'''
E(x) = (Ax + B) % N
N: size of Symbols
'''

def affine_encrypt(text, key):
    keyA, keyB = getKey(key)
    encrypted_text = ""
    for symbol in text:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            encrypted_text += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            encrypted_text += symbol
    return encrypted_text

def affine_decrypt(text, key):
    keyA, keyB = getKey(key)
    decrypted_text = ""
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in text:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            decrypted_text += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            decrypted_text += symbol
    return decrypted_text

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

def main():
    key = getRandomKey()

    #open the plain text file
    fileref = open("aMessageByGeorgeCarlin.txt","r")

    #Open/Create an encrypted file
    affine_encrypted_message = affine_encrypt(fileref.read(), key)
    encrypted_file = open("affine_encrypted_message.txt","w")
    encrypted_file.write(affine_encrypted_message)
    encrypted_file.close()

    #Open/Create a decrypted file
    decrypted_file = open("affine_decrypted_message.txt","w")
    affine_decrypted_message = affine_decrypt(affine_encrypted_message, key)
    decrypted_file.write(affine_decrypted_message)
    decrypted_file.close()

    fileref.close()
  
if __name__ == '__main__': 
    main() 


