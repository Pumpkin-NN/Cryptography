data_matrix =   [
                    [2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]
                ]

def fill_zeros(data_val):
    return bin(int(data_val, 16))[2:].zfill(8)
           

input_hex = [0xd4, 0xbf, 0x5d, 0x30]

input_bin = []
for i, bin_num in enumerate(input_hex):
    bin_num = bin(input_hex[i])[2:].zfill(8)
    print(bin_num)
    bin_num = int(bin_num, 2)
    input_bin.append(bin_num)
print(input_bin)



output = []
for col in data_matrix:
    print("+++++++++++++++++++++++\nThe {} round\n\n".format(col))
    result_row_1 = []
    for i, row in enumerate(col):
        if row == 2:
            print("2")

            a = input_bin[i]
            a = bin(input_bin[i])[2:].zfill(8)
            """
            print("AAAAAAAAAAAAAAAAA\n")
            print("a = {}".format(a))
            print(type(a))
            print("\nAAAAAAAAAAAAAAAA")
            """
            if int(a[0]) == 1:
                a = input_bin[i] << 1
                a = bin(a)[3:].zfill(8)
                #print("I am a leftshifted a: {}".format(a))
                a = int(a, 2)
                xor_row_1 = a ^ 0x1b
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)
                #print("I am == 1: {}".format(xor_row_1))
            else:
                a = input_bin[i] << 1
                a = bin(a)[2:].zfill(8)
                a = int(a, 2)
                xor_row_1 = a
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)
                #print("I am == 0: {}".format(xor_row_1))
                xor_row_1 = a
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)


        elif row == 3:
            print("3")
            b = input_bin[i]
            b = bin(input_bin[i])[2:].zfill(8)
            """
            print("BBBBBBBBBBBBBBBBBB\n")
            print("b = {}".format(b))
            print(type(b))
            print("\nBBBBBBBBBBBBBBBBBBB")
            """

            if int(b[0]) == 1:
                b = input_bin[i] << 1
                b = bin(b)[3:].zfill(8)
                #print("I am a leftshifted b: {}".format(b))
                b = int(b, 2)
                xor_row_2 = b ^ 0x1b ^ input_bin[i]
                xor_row_2 = bin(xor_row_2)[2:].zfill(8)
                #print("I am == 1: {}".format(xor_row_2))
            else:
                b = input_bin[i] << 1
                b = bin(b)[2:].zfill(8)
                #print("I am a leftshifted b: {}".format(b))
                b = int(b, 2)
                xor_row_2 = b ^ input_bin[i]
                xor_row_2 = bin(xor_row_2)[2:].zfill(8)
                #print("I am == 0: {}".format(xor_row_2))
            #print(xor_row_2)
        else:
            print("1")
            result_1 = bin(input_bin[i])[2:].zfill(8)
            result_row_1.append(result_1)
            print("______the result_row_1 is:{}".format(result_row_1))
            if len(result_row_1) < 2:
                continue
            else:
                xor_row_3 = result_row_1[0]
                print("\n\n****************************\n")
                print("I am xor_row_3: {}".format(xor_row_3))
                print("\n\n****************************\n")
                xor_row_4 = result_row_1[1]
                print("\n\n****************************\n")
                print("I am xor_row_4: {}".format(xor_row_4))
                print("\n\n****************************\n")
    print("\nit's a column\n")
    print("============\nXOR Results")
    print("xor_row_1:{}".format(xor_row_1))
    print("xor_row_2:{}".format(xor_row_2))
    print("xor_row_3:{}".format(xor_row_3))
    print("xor_row_4:{}".format(xor_row_4))
    xor_result = int(xor_row_1, 2) ^ int(xor_row_2, 2) ^ int(xor_row_3, 2) ^ int(xor_row_4, 2)
    xor_result = hex(xor_result)
    print(xor_result)
    output.append(xor_result)
print(output)