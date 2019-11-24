import copy
import math

IndexTable = ["A","B","C","D","E","E","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z","' '",".","?","$","0","1","2","3","4","5",
              "6","7","8","9"]



def string2num(*List):
    message = copy.deepcopy(*List)
    num = []
    for i in message:
        for j in IndexTable:
            if i == j:
                num.append(IndexTable.index(j))
    return num

def plaintext_digraphs(*List):
    List = copy.deepcopy(*List)
    digraphs = []
    for i in range(len(List)):
        if i % 2 != 0:
            continue
        if i + 1 == len(List):
            break
        else:
            num = 40 * (List[i]) + 1 * (List[i+1])
            num = (num ** 179) % 2047
        digraphs.append(num)
    return digraphs

def ciphertext_trigraphs(*List):
    List = copy.deepcopy(*List)
    trigraphs = []
    for i in range(len(List)):
        a = List[i] // (40**2)
        b = ( List[i] - (a * List[i]) ) // 40
        c = ( List[i] - (a * List[i]) ) % 40
        trigraphs.append(a)
        trigraphs.append(b)
        trigraphs.append(c)
    return trigraphs

def num2string(*List):
    List = copy.deepcopy(*List)
    # Convert it into the text
    text = []
    for j in range(len(List)):
        text.append(IndexTable[List[j]])
    text = ''.join(text)
    print(text)
    print("")

def RSA(pub_key,n):
    floor_number = math.floor(math.sqrt(n))
    #print(floor_number)
    # while True:
    #     r = n % floor_number
    #     print("r:{}".format(r))
    #     if r == 0:
    #         print(r)
    #         break
    #     floor_number = n % r
    #     print("floor_number:{}".format(floor_number))
    #     if r == 0:
    #         print(r)
    #         break

    for i in range(1, floor_number):
        if n % i == 0 and i != 1:
            p = i
            q = n // i

    phi_n = (p-1) * (q-1)

    for j in range(1, n):
        if (j * pub_key) % phi_n == 1:
            pri_key = j

    return pri_key

def ciphertext_sevengraphs(Encrypted_Message,pri_key,n):
    segment = len(Encrypted_Message) // 7
    cut = len(Encrypted_Message) // segment

    first_part = Encrypted_Message[:cut]
    second_part = Encrypted_Message[cut:]

    ciphertext_first = string2num(first_part)
    ciphertext_second = string2num(second_part)
    
    for i in range(len(ciphertext_first)):
        if i + 6 == len(ciphertext_first):
            break
        cipher_first_nums = (26**6) * ciphertext_first[i] + \
                            (26**5) * ciphertext_first[i+1] + \
                            (26**4) * ciphertext_first[i+2] + \
                            (26**3) * ciphertext_first[i+3] + \
                            (26**2) * ciphertext_first[i+4] + \
                            (26**1) * ciphertext_first[i+5] + \
                            (26**0) * ciphertext_first[i+6]

    for j in range(len(ciphertext_second)):
        if j + 6 == len(ciphertext_second):
            break
        cipher_second_nums = (26**6) * ciphertext_second[j] + \
                             (26**5) * ciphertext_second[j+1] + \
                             (26**4) * ciphertext_second[j+2] + \
                             (26**3) * ciphertext_second[j+3] + \
                             (26**2) * ciphertext_second[j+4] + \
                             (26**1) * ciphertext_second[j+5] + \
                             (26**0) * ciphertext_second[j+6]

    #p1 = (cipher_first_nums ** pri_key) % n

    # PowerMod Calculator
    p1 = 45005201 

    #p2 = (cipher_second_nums ** pri_key) % n

    # PowerMod Calculator
    p2 = 56094542

    p = [p1, p2]
    return p

def plaintext_sixgraphs(*List):
    List = copy.deepcopy(*List)
    text = []
    for i in List:
        sixth_block = i // (26**5)
        text.append(sixth_block)

        r1 = i % (26**5)
        fifth_block = r1 // (26**4)
        text.append(fifth_block)

        r2 = r1 % (26**4)
        fourth_block = r2 // (26**3)
        text.append(fourth_block)

        r3 = r2 % (26**3)
        third_block = r3 // (26**2)
        text.append(third_block)

        r4 = r3 % (26**2)
        second_block = r4 // (26**1)
        text.append(second_block)

        r5 = r4 % (26**1)
        first_block = r5
        text.append(first_block)
    return text

if __name__== "__main__":
    # Problem #1 (1)
    print("\n-------------Problem #1-------------\n")
    message = "SEND $7500"
    message = list(message)
    num = string2num(message)
    digraphs = plaintext_digraphs(num) # This is correct!
    print("The Plaintext is:\nSEND $7500\n")
    print("The Ciphertext is:")
    trigraphs = ciphertext_trigraphs(digraphs)
    num2string(trigraphs)
    
        # Validation
    #num = string2num("BAAAVOBAAAJEAR0")
    #cipher = plaintext_digraphs(num)
    #print(cipher)
    # Problem #1 (2)
    private_key = RSA(179, 2047)
    print("The decipher key is:\n({}, {})".format(2047, private_key))

    # Problem #2
    print("\n-------------Problem #2-------------\n")
        # The Encrypted Message
    Encrypted_Message = "BNBPPKZAVQZLBJ"
    Encrypted_Message = list(Encrypted_Message)
        # Find the private key
    #pri_key = RSA(3602561,536813567)
    n = 536813567
    pri_key = 201934721
    p = []
    p = ciphertext_sevengraphs(Encrypted_Message, pri_key, n)
    plaintext = []
    plaintext = plaintext_sixgraphs(p)
    print("The Decrypted Message is: ")
    num2string(plaintext)

