import copy
def table():
    table = []
    for i in range(65, 91):
        letter = chr(i)
        if i == ord("J"):
            continue
        table.append(letter)
    return table

def playfair_cipher(cipher,*List):
    List = copy.deepcopy(*List)
    cipher = list(cipher)
      
    for i in cipher[::-1]:
        List.insert(0,i)
    
    new_list = []  
    for j in List:
        if j in new_list:
            continue
        new_list.append(j)
    print(new_list)


if __name__== "__main__":
    table = table()
    cipher = input("Please type in the cipher:\n")
    print("The new index table is:")
    playfair_cipher(cipher, table)