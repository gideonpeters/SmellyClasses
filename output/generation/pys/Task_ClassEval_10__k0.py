class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = ''.join(filter(lambda x: x in ['0', '1'], binary_string))

    def calculate_binary_info(self):
        zeroes = self.binary_string.count('0') / len(self.binary_string)
        ones = self.binary_string.count('1') / len(self.binary_string)
        return {'Zeroes': zeroes, 'Ones': ones, 'Bit length': len(self.binary_string)}

    def convert_to_ascii(self):
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            ascii_string += chr(int(byte, 2))
        return ascii_string

    def convert_to_utf8(self):
        utf8_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            utf8_string += chr(int(byte, 2))
        return utf8_string
