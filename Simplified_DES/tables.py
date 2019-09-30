
#Permute the key
#Let the 10-bit key be designated as (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10)
P10 = [3,5,2,7,4,10,1,9,8,6]

#Apply P8, which picks out and permutes 8 of the 10 bits
P8 = [6,3,7,4,8,5,10,9]


#Permute the 8-bit block of plaintext using the IP function
IP = [2,6,3,1,4,8,5,7]

#f function: Expansion/Permutation Operation
E_P = [4,1,2,3,2,3,4,1]

#from the S0 and S1, a further permutation
P4 = [2,4,3,1]

#At the end of the algorithm, the inverse permutation is used:
IP_1 = [4,1,3,5,7,2,8,6]