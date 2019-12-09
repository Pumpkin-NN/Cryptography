import random
import math



def affine_encrypt(a, b):
  for i in range(26):
    print(chr(i+ord('A')) + ": " + chr(((a*i+b)%26)+ord('A')))

def affine_decrypt(a_1, b):
    for num in range(1, 100):
        if (a_1 * num) % 26 == 1:
            a_1 = num
            break
    
    for i in range(26):
        print(chr(((a_1*(i-b))%26)+ord('A')) + ": " + chr(i+ord('A')))

#An example call
affine_encrypt(5, 8)
print("------------------------------------")
affine_decrypt(5, 8)

'''
def affine_encrypt(a, b, text):
    result = ''
    for letter in text:
        i = ord(letter) - 65
        result = str(chr((i+ord('A'))) + ": " + str(chr(((a*i+b)%26)+ord('A'))))
        return result
    

def affine_decrypt(a, b, text):
    for num in range(1, 100):
        if (a * num) % 26 == 1:
            a = num
            break
        break
    
    for letter in text:
        result = ''
        i = ord(letter) - 65
        result = str(chr(i+ord('A')) + ": " + str(chr(((a*(i-b))%26)+ord('A'))))
    print(result)


if __name__ == "__main__":
    text = list(input("type: "))

    b = random.randrange(1, 26)

    while True:
        a = random.randrange(1, 26)
        if math.gcd(a, 26) == 1 and a != 26:
            a = a
            break

    #An example call
    print(affine_encrypt(15, 7, text))
    print("------------------------------------")
    cipher = affine_encrypt(7, 7, text)
    affine_decrypt(a, b, cipher)
'''