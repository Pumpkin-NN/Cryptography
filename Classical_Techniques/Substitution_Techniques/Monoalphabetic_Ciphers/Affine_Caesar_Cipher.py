import random
import math

ALPHABET = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# m = [1, 26]
m = random.randrange(1, 26)

# Find a
while True:
    a = random.randrange(1, 26)
    if math.gcd(a,26) == 1 and a != m:
        a = a
        break

# encrypt the message
def affine_cipher_encryption(plaintext):
    
    # 1 <= b and b <= m
    b = m
    print("b value:{}, a value:{}".format(b, a))
    # Initial ciphertext
    ciphertext = ''

    # Affine Caesar Cipher Algorithm
    for letter in plaintext:
        # C = (a * P + b) % m
        Mod_1 = a * (ord((''.join(letter)))-65) + b
        #print("Mod_1:{}".format(Mod_1))
            
        # M range in [0, 25], an alphabet size
        Mod_2 = m
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

    # Type in the plain text
    plaintext = list(input("Please enter the text: "))

    # Call Affine Ceasar Cipher Function
    affine_cipher_encryption(plaintext)

