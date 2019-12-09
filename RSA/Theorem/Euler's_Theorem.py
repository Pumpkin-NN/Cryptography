import math

# Global Variable
NUM = 100


'''
This is the function to:

#1 Find out the coprime numbers of a random number.

#2 Count the modolus of the coprime numbers of the random number and the random number.

Input: number(int)
Output: modulos(int)

'''
def Euler_Algorithm(NUM):
    for NUM in range(2, 100):
        print("\n*****************************************************\n")
        print("The number is: {}".format(NUM))
        co_prime_numbers = []
        # Find the co-prime numbers
        for i in range(1, NUM):
            if math.gcd(i, NUM) == 1:
                co_prime_numbers.append(i)
        print("co_prime Numbers: {}".format(co_prime_numbers))


        ''' Method 1
        for j in range(len(co_prime_numbers)):
            for k in range(len(co_prime_numbers)):
                if co_prime_numbers[j] < co_prime_numbers[k]:
                    if (co_prime_numbers[j] * co_prime_numbers[k]) % NUM == 1 or (co_prime_numbers[j] * co_prime_numbers[k]) % NUM == NUM - 1:
                        if co_prime_numbers[j] + co_prime_numbers[k] == NUM:
                            print(co_prime_numbers[j], co_prime_numbers[k])
                        else:
                            print("The rest: {}, {}".format(co_prime_numbers[j], co_prime_numbers[k]))
        '''

        # Multiply the first element and the last one
        # Making a list of the middle numbers
        middle_numbers = []
        first_last_modulo = 1
        for j in range(len(co_prime_numbers)):
            if co_prime_numbers[j] < co_prime_numbers[-1 - j]:
                if co_prime_numbers[j] == co_prime_numbers[0]:
                    first_last_modulo = (co_prime_numbers[j] * co_prime_numbers[-1 - j]) % NUM
                    if first_last_modulo == NUM - 1:
                        first_last_modulo = -1
                        print("the first number times the last number, and modulo is: {}".format(first_last_modulo))
                    continue
                middle_numbers.append(co_prime_numbers[j])
                middle_numbers.append(co_prime_numbers[-1 - j])
        #print(middle_numbers)

        # Multiply the middle elements
        multiply_total = 1
        middle_modulo = 1
        for n in range(len(middle_numbers)):
            multiply_total = multiply_total * middle_numbers[n]
            middle_modulo = multiply_total % NUM
            if middle_modulo == NUM - 1:
                middle_modulo = -1

        print("The middle module is :{}".format(middle_modulo))

        # Find out the overall modulo
        final_modulo = first_last_modulo * middle_modulo
        print("The overall modulo is: {}".format(final_modulo))
        print("*****************************************************\n")

Euler_Algorithm(NUM)