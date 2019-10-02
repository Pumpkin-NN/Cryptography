class BinNumber():

    def __init__(self, value, val_type, number_of_bits):

        if number_of_bits == 0: # Empty BinNumber
            self.value = ""

        elif val_type == 'hex':
            # Convert hex to binary string
            self.value = bin(int(value, 16))[2:].zfill(number_of_bits)

        elif val_type == 'bin':
            # Ensure that the binary string has the right number of bits
            self.value = value.zfill(number_of_bits)

        elif val_type == 'dec':
            # Convert dec to binary string
            self.value = bin(value)[2:].zfill(number_of_bits)

        self.val_type = val_type
        self.number_of_bits = number_of_bits

    def __getitem__(self, items):
        # self[items]
        return self.value[items]

    def __lshift__(self, other):
        # Left Circular shift (self << other)
        
        self.value = self.value[other:] + self.value[0:other]

        return BinNumber(self.value, 'bin', self.number_of_bits)

    def __xor__(self, other):
        # self ^ other

        # Checking for same class
        assert isinstance(other, BinNumber), "Not the same class!"
        
        result = []
        for index, letter in enumerate(self.value):
            
            if other.value[index] == letter:
                result.append('0')

            else:
                result.append('1')

        result = "".join(result)
        return BinNumber(result, 'bin', self.number_of_bits)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __add__(self, other):
        assert isinstance(other, BinNumber), "Summing wrong classes"
        return BinNumber(self.value + other.value, 'bin', self.number_of_bits + other.number_of_bits) 

    def transformation(self, table):

        result = []
        for bit_location in table:
            result.append(self.value[bit_location-1])

        result = "".join(result)

        return BinNumber(result, "bin", len(table))

    def repr_hex(self):
        return hex(int(self.value, 2))[2:].zfill(round(self.number_of_bits / 4))

    def split(self):
        half_value = round(self.number_of_bits / 2)
        return BinNumber(self.value[:half_value], 'bin', half_value), BinNumber(self.value[half_value:], 'bin', half_value)

    def split_8(self):
        segmented_bin = [BinNumber(self.value[i:i+6], 'bin', round(self.number_of_bits / 8)) for i in range(0, len(self.value), 6)]
        return segmented_bin
