import copy
def table():
    table = []
    for i in range(65, 91):
        letter = chr(i)
        table.append(letter)
    return table

def vigenere_cipher(*List):
    List = copy.deepcopy(*List)

    nest_list = []
    nested_list = []
    for num,ele in enumerate(List):
        nest_list.append(nested_list)
        for index in ele:
            nested_list.append(index)      
    
    shift_list = []
    for num,subList in enumerate(nest_list):
        # Rotate List elements
        subList = subList[num:] + subList[:num]
        shift_list.append(subList)  
    return shift_list

if __name__== "__main__":
    table = table()
    shift_list = vigenere_cipher(table)
    print(shift_list)