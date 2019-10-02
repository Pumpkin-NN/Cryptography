# Imports 

from BinNumber import BinNumber
import global_variables as glo_var

#---------------------------

# functions

def s_box(left, right):

    segments = [left, right] # BinNumber
    result = BinNumber(0, 'bin', 0)

    for s_box, segment in zip(glo_var.S_BOX, segments):
        col = int(segment[0] + segment[-1], 2)
        row = int(segment[1] + segment[2], 2)

        value = s_box[row][col]
        result += BinNumber(value, 'dec', 2)

    return result

#---------------------------------------------------------------
# Main 

key = BinNumber('0111111101','bin', 10)
cipher = BinNumber('10100010', 'bin', 8)

# Initial Permutation
permutated_cipher = cipher.transformation(glo_var.IP)

# Split the Initial cipher into two halves(left, right)
IP_left, IP_right = permutated_cipher.split()
print(IP_left, IP_right)

# Permutate the right part
permutated_IP_right = IP_right.transformation(glo_var.E)

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

#===========================================PART I

# Expand the IP_right
ex_IP_right = permutated_IP_right.transformation(glo_var.E)

# 'ex_IP_right' XOR 'K2'
xor_IP_right = (ex_IP_right) ^ (k2)
print(xor_IP_right)

# split xor_IP_right
k2_IP_left, k2_IP_right = xor_IP_right.split()
print(k2_IP_left, k2_IP_right)

# S box(k2)
s_result_k2 = s_box(k2_IP_left, k2_IP_right)

# P4 permutation(k2)
permutated_p4_k2 = s_result_k2.transformation(glo_var.P4)

# IP_left XOR P4
xor_P4 = (IP_left) ^ permutated_p4_k2
print("xor_P4:{}".format(xor_P4))

# SW function
sw =  IP_right + xor_P4
print("-----------------------")
print("sw:{}".format(sw))
print("-----------------------")


#=============================================PART II
# Expand the right part again
ex_sw_right = xor_P4.transformation(glo_var.E)

# 'permutated_sw_right' XOR 'K1'
xor_sw_right = (ex_sw_right) ^ (k1)

# split xor_sw_right into two halves
k1_sw_left, k1_sw_right = xor_sw_right.split()

#S box(k1)
s_result_k1 = s_box(k1_sw_left, k1_sw_right)

# P4 permutation(k1)
permutated_p4_k1 = s_result_k1.transformation(glo_var.P4)

# 'P4 permutation(k1)' XOR 'IP_right'
xor_P4_K2 = (permutated_p4_k1) ^ (IP_right)

# XOR result
xor_result = xor_P4_K2 + xor_P4

#Final permutation
fp = xor_result.transformation(glo_var.IPi)
print('\n\n')
print("the Cipher is:{}".format(fp))