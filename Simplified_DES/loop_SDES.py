# Imports 

from BinNumber import BinNumber
import global_variables as glo_var

#---------------------------

# functions

def s_box(left, right):

    segments = [left, right] # BinNumber
    result = BinNumber(0, 'bin', 0)

    for s_box, segment in zip(glo_var.S_BOX, segments):
        print("===================")
        print("Segment: {}".format(segment))
        row = int(segment[0] + segment[-1], 2)
        col = int(segment[1] + segment[2], 2)

        print("row:{}".format(row))
        print("col:{}".format(col))

        value = s_box[row][col]
        print("value:{}".format(value))
        result += BinNumber(value, 'dec', 2)
    
    print("=========================")
    print("result:{}".format(result))
    print("=========================")

    return result

#---------------------------------------------------------------
# Main 

key = BinNumber('0111111101','bin', 10)
cipher = BinNumber('10100010', 'bin', 8)

#============================================
# Key Generation

permutated_key = key.transformation(glo_var.P10)
left, right = permutated_key.split()

# Bit Shift (1)
left, right = left << 1, right << 1
combined = left + right
k1 = combined.transformation(glo_var.P8)
print("K1: {}".format(k1))

# Bit Shift (2+1)
left, right = left << 2, right << 2
combined = left + right
k2 = combined.transformation(glo_var.P8)
print("K2: {}".format(k2))

#============================================
# DES Algorithm

#Decrypt using keys
K = [k2, k1]

for key in K:

    if key == K[0]:
        # Permutation
        permutated_cipher = cipher.transformation(glo_var.IP)
        print("permutated_cipher:{}".format(permutated_cipher))
    else:
        permutated_cipher = sw

    # Split the Initial cipher into two halves(left, right)
    left, right = permutated_cipher.split()
    print(left, right)

    # Split the Initial cipher into two halves(left, right)
    left, right = permutated_cipher.split()
    print(left, right)
    # Permutate the right part
    permutated_right = right.transformation(glo_var.E)
    print("e: {}".format(permutated_right))
    # 'ex_right' XOR 'Key'
    xor_right = (permutated_right) ^ (key)
    print("a: {}".format(xor_right))

    # split xor_right
    key_left, key_right = xor_right.split()
    print(key_left, key_right)

    # S box
    s_result = s_box(key_left, key_right)

    # P4 permutation
    permutated_p4 = s_result.transformation(glo_var.P4)

    # left XOR P4
    xor_P4 = (left) ^ permutated_p4

    if key == K[0]:
        # SW function
        sw =  right + xor_P4
        print("-----------------------")
        print("sw:{}".format(sw))
        print("-----------------------")

# XOR result
xor_result = xor_P4 + right
print("The xor_result is:{}".format(xor_result))


#Final permutation
fp = xor_result.transformation(glo_var.IPi)
print('\n\n')
print("the Cipher is:{}".format(fp))

# convert the binary to letters
fp_left, fp_right = fp.split()

# make the BinNumber to integer
fp_left_int, fp_right_int = int(fp_left.value, 2), int(fp_right.value, 2)
print(fp_left_int, fp_right_int)

fp_left_letter, fp_right_letter = chr(fp_left_int + ord('A')), chr(fp_right_int + ord('A'))

fp_letter = fp_left_letter + fp_right_letter
print("the Plaintext is:{}".format(fp_letter))
