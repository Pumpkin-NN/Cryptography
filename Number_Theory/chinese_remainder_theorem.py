# Method 1, find all the inverse, if and only if the inverses exists
# This method is limited!
mport math
from find_inverse import find_inverse
def CRT(Reminder, Divisor):
    # Check if each element in Divisor coprime or not
    if math.gcd(Divisor[0],Divisor[1]) == 1 and \
       math.gcd(Divisor[0],Divisor[2]) == 1 and \
       math.gcd(Divisor[1],Divisor[2]) == 1:
        # Find the product of the divisors
        product = 1
        for ele in Divisor:
            product = product*ele
        print("The product is: {}".format(product))

        # Create a new list
        List = []
        for i in Divisor:
            new_ele = product // i
            List.append(new_ele)
        print("The List is: {}".format(List))

        # Analyse each reminder related to another specific element
        # d: divisor
        # e: each element
        Inverse = []
        for d,e,re in zip(Divisor, List, Reminder):
            inverse_num = find_inverse(d, e)
            Inverse.append(inverse_num)
        print("The List of inverse is: {}".format(Inverse))

        Sum_List = []
        for inv,l,r in zip(Inverse, List, Reminder):
            sum_num = inv * l * r
            Sum_List.append(sum_num)
        print("The sum list is: {}".format(Sum_List))

        Num = 0
        for j in Sum_List:
            Num = (Num + j) % product

        # Validation
        Reminder_List = []
        for di in Divisor:
            reminder_num = Num % di
            Reminder_List.append(reminder_num)
        if Reminder_List == Reminder:
            print("The result is true and this is only true if the inverses exists\nAnd the result is: {}".format(Num))
        else:
            print("The result is wrong, because some inverses does not exist")

    else:
        print("The divisors should be coprime to each other!")
if __name__ == '__main__': 
    # Sample 1
    CRT([3,1,6],[5,7,8])

    print("------------------------------")

    # Sample 2
    CRT([2,2,1],[3,4,5])

