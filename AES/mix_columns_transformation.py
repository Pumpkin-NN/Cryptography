data_matrix =   [
                    [2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]
                ]

input_hex = [0x67, 0x89, 0xAB, 0xCD]

input_bin = []
for i, bin_num in enumerate(input_hex):
    bin_num = bin(input_hex[i])[2:].zfill(8)
    print(bin_num)
    bin_num = int(bin_num, 2)
    input_bin.append(bin_num)
print(input_bin)

output = []
for col in data_matrix:
    result_row_1 = []
    for i, row in enumerate(col):
        # If the Row Number is 02
        if row == 2:
            a = input_bin[i]
            a = bin(input_bin[i])[2:].zfill(8)
            if int(a[0]) == 1:
                a = input_bin[i] << 1
                a = bin(a)[3:].zfill(8)
                a = int(a, 2)
                xor_row_1 = a ^ 0x1b
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)
            else:
                a = input_bin[i] << 1
                a = bin(a)[2:].zfill(8)
                a = int(a, 2)
                xor_row_1 = a
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)
                xor_row_1 = a
                xor_row_1 = bin(xor_row_1)[2:].zfill(8)
        # If the Row Number is 03
        elif row == 3:
            b = input_bin[i]
            b = bin(input_bin[i])[2:].zfill(8)
            if int(b[0]) == 1:
                b = input_bin[i] << 1
                b = bin(b)[3:].zfill(8)
                b = int(b, 2)
                xor_row_2 = b ^ 0x1b ^ input_bin[i]
                xor_row_2 = bin(xor_row_2)[2:].zfill(8)
            else:
                b = input_bin[i] << 1
                b = bin(b)[2:].zfill(8)
                b = int(b, 2)
                xor_row_2 = b ^ input_bin[i]
                xor_row_2 = bin(xor_row_2)[2:].zfill(8)
        # If the Row Number is 01
        else:
            result_1 = bin(input_bin[i])[2:].zfill(8)
            result_row_1.append(result_1)
            if len(result_row_1) < 2:
                continue
            else:
                xor_row_3 = result_row_1[0]
                xor_row_4 = result_row_1[1]
    # XOR Operation
    xor_result = int(xor_row_1, 2) ^ int(xor_row_2, 2) ^ int(xor_row_3, 2) ^ int(xor_row_4, 2)
    xor_result = hex(xor_result)
    output.append(xor_result)
#Ouput the Final Result
print(output)

# Final Result is ['0x28', '0x45', '0xef', '0xa']