def Brute_Force(Reminder, Divisor):
    Nums = []
    for r, d in zip(Reminder, Divisor):
        for m in range(2, 1000):
            if m % d == r:
                Nums.append(m)
            # print(Nums)
    num = max(set(Nums), key = Nums.count) 
    print(num)

    # Validation
    Reminder_List = []
    for di in Divisor:
        reminder_num = num % di
        Reminder_List.append(reminder_num)
    if Reminder_List == Reminder:
        print("The result is true and and the result is: {}\n".format(num))
    else:
        print("The result is wrong")    

if __name__ == '__main__': 
    # Sample 1
    Brute_Force([1,1,1,1,1,0],[2,3,4,5,6,7])

    # Sample 2
    Brute_Force([2,2,1],[3,4,5])

    # Sample 3
    Brute_Force([3,4,7],[4,7,9])

    # Sample 4
    Brute_Force([2,3,2],[3,5,7])

    # Sample 5
    Brute_Force([1,1,0],[2,3,7])