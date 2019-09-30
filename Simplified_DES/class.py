class Hex_to_Bin:
    def __init__(self):
    
    #Transfer Hexadecimal to Binary
    #Input a hexdata
        self.input = input("Please input a hexdata: ")
    #Transform
        self.bin_num = bin(int(self.input, 16))[2:].zfill(8)
    #Print out the binary form
        print("The Binary form is: ", self.bin_num)

C1 = Hex_to_Bin()