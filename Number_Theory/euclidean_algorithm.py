
def euclidean_algorithm(a, b):
    while b > 0:
        print("({}, {})\n".format(a, b))
        r = a % b
        a = b
        if r > 0:
            b = r
        else:
            break
    return b

print("\nThe first test: ")
result1 = euclidean_algorithm(973, 301)
print("The result is: {}".format(result1))

print("\n\nThe second test: ")
result2 = euclidean_algorithm(27, 21)
print("The result is: {}".format(result2))
