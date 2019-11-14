
def extended_euclidean_algorithm(a, b):
    # Initial s = 1
    s = 1
    list_s = []
    list_t = []
    # Algorithm
    while b > 0:
        #print("({}, {})\n".format(a, b))

        # Find the remainder of a, b
        r = a % b
        #print("the r is {}".format(r))

        #print("the a is {}".format(a))
        #print("the b is {}".format(b))

        if r > 0:
            # The t expression
            t = (r - (a * s)) // b 
            #print("the s is {}".format(s))
            #print("the t is {}".format(t))
            list_t.append(t)
            list_s.append(s)

        # Use b to be the new a
        a = b
        if r > 0:
            # Use the remainder to be the new b
            b = r

            #print("the r is {}".format(r))
            #print("the a is {}".format(a))
            #print("the b is {}".format(b))
        else:
            break
        #print("--------------------------------------")

    #print(list_s, list_t)

    # Find the coefficients s and t
    for i in range(len(list_t)):
        if i+1 < len(list_t):
            # Find the coefficient t
            t = list_t[0] + (list_t[(len(list_t)-1)] * s)
            print("t = ", t)

            # Find the coefficient s
            s = list_s[i] + list_t[i] * list_t[i+1]
            #print("s = ", s)
    return t
