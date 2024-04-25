class NumberWordFormatter:
    def __init__(self):
        self.ones = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
        self.teens = ['TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
        self.tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']
        self.suffixes = ['', 'THOUSAND', 'MILLION', 'BILLION']

    def format(self, number):
        if number is None:
            return ""
        if isinstance(number, int):
            return self.format_integer(number)
        elif isinstance(number, float):
            return self.format_float(number)

    def format_integer(self, number):
        if number == 0:
            return "ZERO ONLY"
        words = self.convert_to_words(str(number))
        return ' '.join(words) + ' ONLY'

    def format_float(self, number):
        integer_part, decimal_part = str(number).split('.')
        integer_words = self.format_integer(int(integer_part))
        decimal_words = self.convert_to_words(decimal_part)
        return f"{integer_words} AND CENTS {' '.join(decimal_words)} ONLY"

    def convert_to_words(self, number_str):
        number_str = number_str.zfill((len(number_str) + 2) // 3 * 3)
        chunks = [number_str[i:i+3] for i in range(0, len(number_str), 3)]
        words = []
        for i, chunk in enumerate(chunks):
            if chunk != '000':
                words += self.trans_three(chunk)
                if len(chunks) - i > 1 and int(chunk) != 0:
                    words.append(self.parse_more(len(chunks) - i - 1))
        return words

    def trans_three(self, number_str):
        words = []
        if number_str[0] != '0':
            words.append(self.ones[int(number_str[0])] + ' HUNDRED')
        if number_str[1:] in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']:
            words.append(self.trans_two(number_str[1:]))
        else:
            words.append(self.tens[int(number_str[1])] + ' ' + self.ones[int(number_str[2])]
                         if number_str[1] != '1' else self.teens[int(number_str[2])])
        return words

    def trans_two(self, number_str):
        if number_str == '00':
            return ''
        elif number_str[0] == '0':
            return self.ones[int(number_str[1])]
        elif number_str[0] == '1':
            return self.teens[int(number_str[1])]
        else:
            return self.tens[int(number_str[0])] + ' ' + self.ones[int(number_str[1])]

    def parse_more(self, power):
        return self.suffixes[power]
