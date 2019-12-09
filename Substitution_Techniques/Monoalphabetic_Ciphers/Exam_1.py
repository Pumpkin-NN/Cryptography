import random
import math

ALPHABET = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# M, an alphabet size
M = 26 

# encrypt the message
def affine_cipher_encryption(a, b, plaintext):
    # Initial ciphertext
    ciphertext = ''

    # Affine Caesar Cipher Encryption Algorithm
    for letter in plaintext:
        # C = (a * P + b) % M
        denominator = a * (ord(letter) - ord('A')) + b
       
        # Find Ciphertext(numbers)
        remainder = (denominator) % M

        # Convert Ciphertext(numbers) to letters
        ciphertext += chr(remainder + ord('A'))

    return(ciphertext)
    
# decrypt the message
def affine_cipher_decryption(a_1, b, ciphertext):
    # Initial plaintext
    plaintext = ''

    # Affine Caesar Cipher Encryption Algorithm
    for letter in ciphertext:
        # P = a_1(c - b) % M
        denominator = a_1 * ((ord(letter) - ord('A')) - b)
        if denominator >= 0:
            denominator = denominator
        else:
            denominator = M + denominator
        
        # Find Plaintext(numbers)
        remainder = (denominator) % M
        
        # Convert Plaintext(numbers) to letters
        plaintext += chr(remainder + ord('A'))

    return(plaintext)

if __name__ == "__main__":

    # Find b
    # For Exam1, the b = 18
    b = random.randrange(1, 26)

    # Find a
    # For Exam1, the a = 7
    while True:
        a = random.randrange(1, 26)
        if math.gcd(a, 26) == 1 and a != M:
            a = a
            break

    # Find the inverse of a
    # For Exam1, the a^1 = 15
    for num in range(1, 100):
        if (a * num) % M == 1:
            a_1 = num
            break

    print("The b is: {}\nThe a is: {}\nThe a_1 is: {}\n".format(b, a, a_1))

    fileref = open("Cipher.txt","r")
    plain_text = open("Plaintext.txt","w")

    # Could set fixed numbers: a_1 = 15, b = 18
    plaintext = affine_cipher_decryption(a_1, b, list(fileref.read()))

    plain_text.write(plaintext)
    fileref.close()
