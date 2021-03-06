# Find the greatest common divisor using the Euclidean Algorithm
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
result2 = euclidean_algorithm(301, 973)
print("The result is: {}".format(result2))

print("\n\nThe third test: ")
result3 = euclidean_algorithm(27, 21)
print("The result is: {}".format(result3))
