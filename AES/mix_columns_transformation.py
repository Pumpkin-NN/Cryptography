data_matrix =   [
                    [2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]
                ]


def mix_columns_transformation(input_hex):
    input_bin = []
    for i, bin_num in enumerate(input_hex):
        bin_num = bin(input_hex[i])[2:].zfill(8)
        bin_num = int(bin_num, 2)
        input_bin.append(bin_num)

    # Return the output    
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
    #Ouput the Final Result output_hex
    output_hex = output
    print("\n\nThe results for the second transformation are: {}\n\n".format(output_hex))
    return output_hex

input_hex1 = [0x67, 0x89, 0xAB, 0xCD]
input_hex2 = [0x77, 0x89, 0xAB, 0xCD]


output_hex1 = mix_columns_transformation(input_hex1)
output_hex2 = mix_columns_transformation(input_hex2)

# Determine how many bits have changed after the mix columns transformation
diff = []
for a, b in zip(output_hex1, output_hex2):
    input_a = int(a, 16)
    input_b = int(b, 16)
    diff_num = input_a ^ input_b
    diff.append(bin(diff_num)[2:])
print("The list of the changed bits is: {}\n\n".format(diff))

diff_list = []
for i in diff:
    i = list(i)
    diff_list.append(i)

print("The every element in the diff_list is: {}\n\n".format(diff_list))

# Because if any bits changed, the XOR result of the input_hex1 values and output_hex values would be 1
count_num = sum(x.count('1') for x in diff_list)
print("The changed bits total are: {}".format(count_num))
