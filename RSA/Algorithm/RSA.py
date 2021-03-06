"""
Author: Nicole
Last modifyed: 11/15 2019
Description: the foundation of the RSA algorithm
"""

import random
from EEA import extended_euclidean_algorithm

# Choose two prime numbers
#P = 17
#Q = 11
# Calculate the N
#N = 2047
N = 536813567

# Function: find the greatest common divisor
def gcd(a, b):
    cds = []
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            cds.append(i)
    gcd = cds[-1]
    return gcd

# Fuction: calculate Φ(N)
def phi_N():
    phi_N = 0
    for i in range(1, N):
        if gcd(i, N) == 1:
            phi_N = phi_N + 1
    return phi_N


# Function: Select e, such that e is relatively prime to Φ(N)
def choose_e(val):
    e_list = []
    for i in range(1, phi_n):
        if gcd(i, phi_n) == 1 and i < phi_n:
            e_list.append(i)
    # Randomly choose a number from the e_list
    #return random.choice(e_list)
    return e_list[2]

# Function: Determine d, such d and e are multiplicative inverse
def determine_d(a, m):
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

# Main Function
if __name__== "__main__":
    # Calculate Φ(N)
    phi_n = phi_N()
    print("phi_n value is: ", phi_n)

    # Select e, we choose 7 in this case
    #e = 179
    e = 3602561
    print("e value is: ", e)

    # Determine d
    d = determine_d(179, phi_n)
    print("Make sure a less than m!") 
    print("Calculate the d is: ", d)

    # The resulting public key
    print("The public key is: [{}, {}]".format(e, N))

    # The resulting private key
    print("The private key is: [{}, {}]".format(d, N))
