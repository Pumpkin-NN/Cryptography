'''
def CRT(Reminder, Divisor):
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

    Sum_List = []
    for r, d, l in zip(Reminder, Divisor, List):
        print(r, d, l)
        if l % d == r:
            Sum_List.append(l)
        elif r == 1:
            Sum_List.append(l+1)
        else:
            m = l % d
            for x in range(1, 100000):
                if (m * x) % d == r:
                    sum_num = l * x
                    Sum_List.append(sum_num)
                    break
    print(Sum_List)

    Num = 0
    for j in Sum_List:
        Num = (Num + j) % product

    # Validation
    Reminder_List = []
    for di in Divisor:
        reminder_num = Num % di
        Reminder_List.append(reminder_num)
    if Reminder_List == Reminder:
        print("The result is true and and the result is: {}\n".format(Num))
    else:
        print("The result is wrong")
'''
Nums = []
def Brute_Force(Reminder, Divisor):
    for r, d in zip(Reminder, Divisor):
        for m in range(2, 1000):
            if m % d == r:
                Nums.append(m)
            # print(Nums)
    num = max(set(Nums), key = Nums.count) 
    print(num)        

if __name__ == '__main__': 
    # Sample 1
    Brute_Force([1,1,1,1,1,0],[2,3,4,5,6,7])
