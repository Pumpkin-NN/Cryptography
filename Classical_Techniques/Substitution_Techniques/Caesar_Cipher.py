# Define Caesar Cipher Encryption
def caesar_cipher_encryption(key, plaintext):
    result = ''
    for letter in plaintext:
        C = (ord(letter) + key)
        result = result + chr(C)
    print(result)

# Define Caesar Cipher Decryption
def caesar_cipher_decryption(key, plaintext):
    caesar_cipher_encryption(key == -key, plaintext)

# Main Function
if __name__== "__main__":

    # Type in the Plain Text
    # Convert the input to List
    plaintext = list(input("Please type in your plaintext: "))

    # key = [1, 25]
    # Generate Random Key
    key = int(input("Please input the key value, and the key scale from 1 to 25: "))

    caesar_cipher_encryption(key, plaintext)
    caesar_cipher_decryption(key, plaintext)
