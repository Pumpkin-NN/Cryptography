import tables

class basic_Operation:
    def __init__(self):
    
    #Transfer Hexadecimal to Binary
    #Input a hexdata
        self.input = input("Please input a hexdata: ")
    #Transform
        self.bin_num = bin(int(self.input, 16))[2:].zfill(8)
    #Print out the binary form
        print("The Binary form is: ", self.bin_num)

    def __xor__(self, other):
        print(E_xor = self.bin_num ^ other.bin_num)
        


class simplified_DES:
    def f_function(self):
        print("h")





if __name__ == "__main__":
    C2 = basic_Operation()

