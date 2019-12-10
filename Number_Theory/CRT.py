import math
def CRT(Reminder, Divisor):
    # Check if each element in Divisor coprime or not
    if math.gcd(Divisor[0],Divisor[1]) == 1 and \
       math.gcd(Divisor[0],Divisor[2]) == 1 and \
       math.gcd(Divisor[1],Divisor[2]) == 1:
        # Find the product of the divisors
        product = 1
        for ele in Divisor:
            product = product*ele
        #print("The product is: {}".format(product))

        # Create a new list
        List = []
        for i in Divisor:
            new_ele = product // i
            List.append(new_ele)
        #print("The List is: {}".format(List))

        Sum_List = []
        for r, d, l in zip(Reminder, Divisor, List):
            if l % d == r:
                Sum_List.append(l)
            else:
                m = l % d
                for x in range(1, 1000):
                    if (m * x) % d == r:
                        sum_num = l * x
                        Sum_List.append(sum_num)
                        break
        #print(Sum_List)

        Num = 0
        for j in Sum_List:
            Num = (Num + j) % product
        
        # Validation
        Reminder_List = []
        for di in Divisor:
            reminder_num = Num % di
            Reminder_List.append(reminder_num)
        if Reminder_List == Reminder:
            print("The result is true and and the result is: {}".format(Num))
        else:
            print("The result is wrong")
        
    else:
        print("The divisors should be coprime to each other!")

if __name__ == '__main__': 
    # Sample 1
    CRT([3,1,6],[5,7,8])

    print("------------------------------")

    # Sample 2
    CRT([2,2,1],[3,4,5])

