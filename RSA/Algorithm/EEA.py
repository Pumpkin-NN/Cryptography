
def extended_euclidean_algorithm(a, b):
    # Initial s = 1
    s = 1
    list_s = []
    list_t = []
    # Algorithm
    while b > 0:
        # Find the remainder of a, b
        r = a % b
        if r > 0:
            # The t expression
            t = (r - (a * s)) // b
            list_t.append(t)
            list_s.append(s)

        # Use b to be the new a
        a = b
        if r > 0:
            # Use the remainder to be the new b
            b = r
        else:
            break

    # Find the coefficients s and t
    for i in range(len(list_t)):
        if i+1 < len(list_t):
            # Find the coefficient t
            t = list_t[0] + (list_t[(len(list_t)-1)] * s)
            # Find the coefficient s
            s = list_s[i] + list_t[i] * list_t[i+1]
        
    return t
