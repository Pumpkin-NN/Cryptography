# A test based on Fermats's Theorem
import random
from random import randrange

# Test N, see if it's a prime or not

N = 37


# Find integer q, and q is an odd number
q_list = []
def find_q():
    for i in range(1, 100):
        if i % 2 == 1:
            q_list.append(i)
    return random.choice(q_list)

def miller_rabin_algorithm(q, a, k):
    if (a**q) % N == 1:
        return "maybe prime"
    for i in range(0, k):
        m = 2 * i * q
        if (a**m) % N == N - 1 or (a**m) % N == -1:
            print("1")
            return "maybe prime"
    
    return "composite number"



if __name__== "__main__":
    q = find_q()
    print(q)


    # Find an integer k, and k > 0
    k = randrange(1, 100)
    print(k)

    # Select a random integer a, and 1 < a < N-1
    a = randrange(1, N-1)
    print(a)

    # TODO algorithm check
    print(miller_rabin_algorithm(3, 4, 7))