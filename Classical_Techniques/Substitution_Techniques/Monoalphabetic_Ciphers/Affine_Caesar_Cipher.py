import random
import math

ALPHABET = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# M, an alphabet size
M = 26 

# encrypt the message
def affine_cipher_encryption(plaintext):

    
    # Initial ciphertext
    ciphertext = ''

    # Affine Caesar Cipher Algorithm
    for letter in plaintext:
        # C = (a * P + b) % m
        Mod_1 = a * (ord((''.join(letter)))-65) + b
        #print("Mod_1:{}".format(Mod_1))
            
        Mod_2 = M
        #print("Mod_2:{}".format(Mod_2))

        # Find Ciphertext(numbers)
        Mod = (Mod_1) % (Mod_2)
        #print("Mod:{}".format(Mod))

        # Convert Ciphertext(numbers) to letters
        ciphertext += chr(Mod + 65)

    print(ciphertext)
    

# decrypt the message
def affine_cipher_decryption():
    pass

if __name__ == "__main__":

    # Find b
    b = random.randrange(1, 26)

    # Find a
    while True:
        a = random.randrange(1, 26)
        if math.gcd(a, 26) == 1 and a != M:
            a = a
            break

    print("b value:{}, a value:{}".format(b, a))

    # Type in the plain text
    plaintext = list(input("Please enter the text: "))

    # Call Affine Ceasar Cipher Function
    affine_cipher_encryption(plaintext)

