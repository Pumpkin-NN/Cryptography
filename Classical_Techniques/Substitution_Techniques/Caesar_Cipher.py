# Define Caesar Cipher Encryption
def caesar_cipher_encryption(key, plaintext):
    result = ''
    for letter in plaintext:
        C = (ord(letter) + key)
        result = result + chr(C)
    print(result)

# Define Caesar Cipher Decryption
def caesar_cipher_decryption(key, ciphertext):
    #caesar_cipher_encryption(key == -key, ciphertext)
    result = ''
    for letter in ciphertext:
        # key == -key 
        C = (ord(letter) - key)
        result = result + chr(C)
    print(result)

# Main Function
if __name__== "__main__":

    # Choice to Encrypt or Decrypt
    choice = input("Do you want to Encrypt or Decrypt? (E/D) :\n")
    
    if(choice == 'E'):
        # Type in the Plain Text
        # Convert the input to List
        plaintext = list(input("Please type in your plaintext:\n"))
        # key = [1, 25]
        # Generate Random Key
        key = int(input("Please input the key value, and the key scale from 1 to 25:\n"))
        caesar_cipher_encryption(key, plaintext)
    else:
        ciphertext = list(input("Please type in your ciphertext:\n"))
        # key = [1, 25]
        # Generate Random Key
        key = int(input("Please input the key value, and the key scale from 1 to 25:\n"))
        caesar_cipher_decryption(key, ciphertext)
        

    
   