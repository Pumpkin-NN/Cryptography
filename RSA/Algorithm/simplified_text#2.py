import copy
import math

IndexTable = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"," ",".","?","$","0","1","2","3","4","5",
              "6","7","8","9"]



def string2num(*List):
    message = copy.deepcopy(*List)
    num = []
    for i in message:
        #print("i: {}".format(i))
        for j in IndexTable:
            if i == j:
                num.append(IndexTable.index(j))
                #print("numerircal: {}".format(num))
    #print("num:{}".format(num))
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

        digraphs.append(num)
    return digraphs

def ciphertext_trigraphs(*List):

    List = copy.deepcopy(*List)
    trigraphs = []
    for i in range(len(List)):
        a = List[i] // (40**2)
        r1 = List[i] - (a * 40**2)
        b = r1 // 40
        c = ( List[i] - (a * 40**2 + b * 40) ) % 40
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
    
    return text

def RSA(pub_key,n):
    floor_number = math.floor(math.sqrt(n))
    for i in range(1, floor_number):
        if n % i == 0 and i != 1:
            p = i
            q = n // i

    phi_n = (p-1) * (q-1)

    for j in range(1, n):
        if (j * pub_key) % phi_n == 1:
            pri_key = j

    return pri_key

def ciphertext_encryption_graphs(Encrypted_Message, blocks, base):
    length = len(Encrypted_Message)
    segment = length // blocks

    print(Encrypted_Message)
    print("length:{}".format(length))
    print("segment:{}".format(segment))
    

    # TODO

    chunks = []
    for i in range(0, len(Encrypted_Message), blocks):
        chunk = Encrypted_Message[i:i+blocks]
        chunk = string2num(chunk)
        chunks.append(chunk)
    print(chunks)

    nums_chuncks = []
    for sub_chuncks in chunks:
        print(sub_chuncks)
        for element in range(len(sub_chuncks)):
            if element + blocks - 1 == len(sub_chuncks):
                break
            chunks_nums = 0
            for index in range(blocks):
                co_num = blocks - 1 - index
                chunks_nums = chunks_nums + (base**index) * sub_chuncks[element + co_num]
                if co_num == 0:
                    num_chunks = chunks_nums
                    nums_chuncks.append(num_chunks)
    print(nums_chuncks)
            # Calculation Procedure
            # chunks_nums = (base**0) * sub_chuncks[k+6] + \
            #               (base**1) * sub_chuncks[k+5] + \
            #               (base**2) * sub_chuncks[k+4] + \
            #               (base**3) * sub_chuncks[k+3] + \
            #               (base**4) * sub_chuncks[k+2] + \
            #               (base**5) * sub_chuncks[k+1] + \
            #               (base**6) * sub_chuncks[k] + \

    
    #p = (chunks_nums ** pri_key) % n

    # # PowerMod Calculator
    # p1 = 45005201 

    # #p2 = (cipher_second_nums ** pri_key) % n

    # # PowerMod Calculator
    # p2 = 56094542

    # p = [p1, p2]
    # return p

def plaintext_decryption_graphs(*List):
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

def encryption_question1(nums):
    result = []
    # Encryption
    for num in nums:
        result.append((num ** 179) % 2047)

    return result


def problem1():
    # Problem #1 (1)
    print("\n-------------Problem #1-------------\n")
    
    message = "SEND $7500"
    message = list(message)
    
    num = string2num(message)
    print("num:{}".format(num))
    digraphs = plaintext_digraphs(num)
    
    print("plaintext: {}".format("".join(message)))
    
    #trigraphs = ciphertext_trigraphs(digraphs)
    trigraphs = encryption_question1(digraphs)
    pri_key = 201934721
    n = 536813567
    num_ciphertext = ciphertext_encryption_graphs(message, 2, 40)
    # ciphertext = num2string(num_ciphertext)
    # print("ciphertext: {}".format(ciphertext))

def problem2():
    # Problem #2
    print("\n-------------Problem #2-------------\n")
    # The Encrypted Message
    Encrypted_Message = "ARHILFKAODSTOSBSTWFQL"
    Encrypted_Message = list(Encrypted_Message)
    # Find the private key
    #pri_key = RSA(3602561,536813567)
    n = 536813567
    pri_key = 201934721
    p = []
    p = ciphertext_encryption_graphs(Encrypted_Message, 7, 26)
    # plaintext = []
    # plaintext = plaintext_sixgraphs(p)
    # text = num2string(plaintext)
    # print("The Decrypted Message is: {}".format(text))

if __name__== "__main__":
    
    problem1()
    problem2()
    


