import copy
# Ceaser Table
def table():
    table = []
    for i in range(65, 91):
        letter = chr(i)
        table.append(letter)
    return table
# Define Caesar Cipher Algorithm
def caesar_cipher_algorithm(key, message, *List):
    List = copy.deepcopy(*List)
    result = ''
    for letter in message:
        if letter == ' ':
            result = result + letter
        else:
            text_num = (List.index(letter) + key)
            text = List[text_num]
            result = result + text
    print(result)

# Main Function
if __name__== "__main__":
    message1 = "GCUA VQ DTGCM"
    message2 = "ZL SNIBEVGR PYNFF VF PBZCHGRE FRPHEVGL"
    table = table()
    for k in range(-25, 0):
        caesar_cipher_algorithm(k, message1, table)
    for k in range(-25, 0):
        caesar_cipher_algorithm(k, message2, table)

    
    
   