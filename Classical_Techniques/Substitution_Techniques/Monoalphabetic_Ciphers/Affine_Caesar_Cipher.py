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
    b = random.randrange(1, 26)

    # Find a
    while True:
        a = random.randrange(1, 26)
        if math.gcd(a, 26) == 1 and a != M:
            a = a
            break

    # Find the inverse of a
    for num in range(1, 100):
        if (a * num) % M == 1:
            a_1 = num
            break


    # Choice to Encrypt or Decrypt
    choice = input("Do you want to Encrypt or Decrypt? (E/D) :\n")
    
    if(choice == 'E' or choice == 'e'):
        # Type in the Plain Text && Convert the input to List
        plaintext = list(input("Please type in your plaintext:\n"))
        cipher_text = ''
        plain_text = ''
        cipher_text = affine_cipher_encryption(a, b, plaintext)
        plain_text = affine_cipher_decryption(a_1, b, cipher_text)
        print("The b is: {}\nThe a is: {}\nThe a_1 is: {}\n".format(b, a, a_1))
        print("The Encryption result is: {}".format(cipher_text))
        print("The Original result is: {}".format(plain_text))
    else:
        if(choice != 'D' and choice != 'd'):
            print("Please enter the method, note as the first letter!")
        else:
            ciphertext = list(input("Please type in your ciphertext:\n"))
            plain_text = ''
            plain_text = affine_cipher_decryption(a_1, b, ciphertext)
            cipher_text = ''
            cipher_text = affine_cipher_encryption(a, b, plain_text)
            print("The b is: {}\nThe a is: {}\nThe a_1 is: {}\n".format(b, a, a_1))
            print("The Decryption result is: {}".format(plain_text))
            print("The Original result is: {}".format(cipher_text))


# Trouble Shot: VERY IMPORTANT
"""
print("\n\n**********************************")

a = 3
b = 3

for num in range(1, 100):
    if (a * num) % M == 1:
        a_1 = num
        break


plaintext = "B"

print("Plaintext: {}".format(plaintext))

ciphertext = affine_cipher_encryption(a,b,plaintext)

print("Ciphertext: {}".format(ciphertext))

new_plaintext = affine_cipher_decryption(a_1,b,ciphertext)

print("Returned plaintext: {}".format(new_plaintext))
"""

    

