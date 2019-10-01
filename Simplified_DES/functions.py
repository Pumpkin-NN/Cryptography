
#Permute the key
#Let the 10-bit key be designated as (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10)
P10 = (3,5,2,7,4,10,1,9,8,6)

#Apply P8, which picks out and permutes 8 of the 10 bits
P8 = (6,3,7,4,8,5,10,9)

#Permute the 8-bit block of plaintext using the IP function
IP = (2,6,3,1,4,8,5,7)

#f function: Expansion/Permutation Operation
EP = (4,1,2,3,2,3,4,1)

#from the S0 and S1, a further permutation
P4 = (2,4,3,1)

#At the end of the algorithm, the inverse permutation is used:
FP = (4,1,3,5,7,2,8,6)

S0 = [
                [1,0,3,2],
                [3,2,1,0],
                [0,2,1,3],
                [3,1,3,2]
           ]
S1  = [
                [0,1,2,3],
                [2,0,1,3],
                [3,0,1,0],
                [2,1,0,3]
           ]   


key = '0111111101'
cipher = '10100010'

def permutation(perm, key):
    permutated_key = ""
    for i in perm:
        permutated_key += key[i-1]
        print(permutated_key)

        return permutated_key

#Operation on K1
def generate_first_key(left_key, right_key):
    left_key_shifted = left_key[1:] + left_key[:1]
    right_key_shifted = right_key[1:] + right_key[:1]
    key_shifted = left_key_shifted + right_key_shifted
    return permutation(P8 , key_shifted)


#Operarion on K2
def generate_second_key(left_key, right_key):
    left_key_shifted = left_key[3:] + left_key[:3]
    right_key_shifted = right_key[3:] + right_key[:3]
    key_shifted = left_key_shifted + right_key_shifted
    return permutation(P8 , key_shifted)

def Sbox(input, sbox):
    row = int(input[0] + input[3], 2)
    column = int(input[1] + input[2], 2)
    return bin(sbox[row][column][2:].zfill(4))

def F(right, subkey):
    expanded_cipher = permutation( EP , right)
    xor_cipher = bin( int(expanded_cipher, 2) ^ int(subkey, 2) )[2:].zfill(8)
    left_xor_cipher = xor_cipher[:4]
    right_xor_cipher = xor_cipher[4:]
    left_xor_cipher = Sbox(left_xor_cipher,  S0 )
    right_xor_cipher = Sbox(right_xor_cipher,  S1 )
    return permutation( P4 , left_xor_cipher + right_xor_cipher)

def f(first_half, second_half, key):
    left = int(first_half, 2) ^ int(F(second_half, key), 2)
    print("Fk: " + bin(left)[2:].zfill(4)+second_half)
    return bin(left)[2:].zfill(4), second_half

p10key = permutation( P10 , key)
print("--------------------------------------")
print(p10key)
print("--------------------------------------")
left = p10key[:len(p10key)//2]
right = p10key[len(p10key)//2:]

first_key = generate_first_key(left, right)
second_key = generate_second_key(left, right)
print("[*] First key: " + first_key)
print("[*] Second key: " + second_key)

permutated_cipher = permutation( IP , cipher)
print("IP: " + permutated_cipher)
first_half_cipher = permutated_cipher[:len(permutated_cipher)//2]
second_half_cipher = permutated_cipher[len(permutated_cipher)//2:]

left, right = f(first_half_cipher,second_half_cipher,second_key)
print("SW: " + right + left)
left, right = f(right, left, first_key)

print("IP^-1: " + permutation( FP , left + right))