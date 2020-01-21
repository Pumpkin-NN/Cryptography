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

# Initial Permutation
permutated_cipher = cipher.transformation(glo_var.IP)
print("permutated_cipher:{}".format(permutated_cipher))

# Split the Initial cipher into two halves(left, right)
IP_left, IP_right = permutated_cipher.split()
print(IP_left, IP_right)

# Permutate the right part
permutated_IP_right = IP_right.transformation(glo_var.E)
print("e: {}".format(permutated_IP_right))

#===========================================PART I

# Expand the IP_right
#ex_IP_right = permutated_IP_right.transformation(glo_var.E)
#print("ex_IP_right:{}".format(ex_IP_right))

# 'ex_IP_right' XOR 'K2'
xor_IP_right = (permutated_IP_right) ^ (k2)
print("a: {}".format(xor_IP_right))

# split xor_IP_right
k2_IP_left, k2_IP_right = xor_IP_right.split()
print(k2_IP_left, k2_IP_right)

# S box(k2)
s_result_k2 = s_box(k2_IP_left, k2_IP_right)

# P4 permutation(k2)
permutated_p4_k2 = s_result_k2.transformation(glo_var.P4)

# IP_left XOR P4
xor_P4 = (IP_left) ^ permutated_p4_k2

# SW function
sw =  IP_right + xor_P4
print("-----------------------")
print("sw:{}".format(sw))
print("-----------------------")


#=============================================PART II
# Expand the right part again
ex_sw_right = xor_P4.transformation(glo_var.E)
print("ex_sw_right is:{}".format(ex_sw_right))

# 'permutated_sw_right' XOR 'K1'
xor_sw_right = (ex_sw_right) ^ (k1)
print("xor_sw_right is:{}".format(xor_sw_right))

# split xor_sw_right into two halves
k1_sw_s0, k1_sw_s1 = xor_sw_right.split()

#S box(k1)
s_result_k1 = s_box(k1_sw_s0, k1_sw_s1)
print("s_result_k1 is {}".format(s_result_k1))

# P4 permutation(k1)
permutated_p4_k1 = s_result_k1.transformation(glo_var.P4)
print("The permutated_p4_k1 is:{}".format(permutated_p4_k1))

# 'P4 permutation(k1)' XOR 'IP_right'
xor_P4_K2 = (permutated_p4_k1) ^ (IP_right)

# XOR result
xor_result = xor_P4_K2 + xor_P4
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

