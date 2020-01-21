import copy
import math

# Create an index table for the later references
IndexTable = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"," ",".","?","$","0","1","2","3","4","5",
              "6","7","8","9"]

# Convert string to numbers
def string2num(*List):
    message = copy.deepcopy(*List)
    num = []
    for element in message:
        for index in IndexTable:
            if element == index:
                num.append(IndexTable.index(index))
    return num

# Convert numbers to string
def num2string(*List):
    List = copy.deepcopy(*List)
    text = []
    for j in range(len(List)):
        text.append(IndexTable[List[j]])
    text = ''.join(text)
    return text

# Useless function, as a reference in this code
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

# Transfer graphs 1
def transfer_graphs(Encrypted_Message, blocks, base):
    length = len(Encrypted_Message)
    segment = length // blocks

    #print(Encrypted_Message)
    #print("length:{}".format(length))
    #print("segment:{}".format(segment))
    
    chunks = []
    for i in range(0, len(Encrypted_Message), blocks):
        chunk = Encrypted_Message[i:i+blocks]
        chunk = string2num(chunk)
        chunks.append(chunk)
    #print(chunks)

    nums_chuncks = []
    for sub_chuncks in chunks:
        #print(sub_chuncks)
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
    #print(nums_chuncks)
    return nums_chuncks
            # Calculation Procedure
            # chunks_nums = (base**0) * sub_chuncks[k+6] + \
            #               (base**1) * sub_chuncks[k+5] + \
            #               (base**2) * sub_chuncks[k+4] + \
            #               (base**3) * sub_chuncks[k+3] + \
            #               (base**4) * sub_chuncks[k+2] + \
            #               (base**5) * sub_chuncks[k+1] + \
            #               (base**6) * sub_chuncks[k] + \

# Transfer graphs 2
def graphs_transfer(blocks, base, *List):
    List = copy.deepcopy(*List)
    plaintext_nums = []
    for i in List:
        remainder = i
        for index in range(blocks):
            co_num = blocks -1 - index
            plaintext_num = remainder // (base ** (co_num))
            remainder = i % (base ** (co_num))
            plaintext_nums.append(plaintext_num)
    #print(plaintext_nums)
    return plaintext_nums

# RSA Algorithm: encryption or decryption
def rsa_algorithm(key, n, *List):
    List = copy.deepcopy(*List)
    results = []
    for num in List:
        result = pow(num, key) % n
        results.append(result)
    return results

# Test the first example
def problem1():
    print("\n-------------example #1-------------\n")
    # Plain Message
    message = "SEND $7500"
    message = list(message)
    print("plaintext: {}".format("".join(message)))

    digraphs = transfer_graphs(message, 2, 40)

    pub_key = 179
    n = 2047
    cipher_num = rsa_algorithm(pub_key, n, digraphs)
    #print(cipher_num)

    encrypted_message_nums = graphs_transfer(3, 40, cipher_num)
    encrypted_message = num2string(encrypted_message_nums)
    print("ciphertext: {}".format(encrypted_message))

# Test the third example
def problem2():
    print("\n-------------example #3-------------\n")
    # The Encrypted Message
    Encrypted_Message = "BNBPPKZAVQZLBJ"
    Encrypted_Message = list(Encrypted_Message)
    
    n = 536813567
    pri_key = 201934721
    cipher_num = []
    cipher_num = transfer_graphs(Encrypted_Message, 7, 26)
    #text_num = rsa_algorithm(pri_key, n, cipher_num)
    # Modular Exponentiation Calculator
    cipher_num = [45005201, 56094542]
    #print("After Modular:{}".format(cipher_num))
    plaintext_nums = graphs_transfer(6, 26, cipher_num)

    print("The decipherd message is:")
    plaintext = num2string(plaintext_nums)
    print(plaintext)

# Main function
if __name__== "__main__":
    problem1()
    problem2()
    
