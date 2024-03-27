class NumberWordFormatter:
    def __init__(self):
        self.ones = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
        self.teens = ['TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
        self.tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']
        self.suffixes = ['', 'THOUSAND', 'MILLION', 'BILLION']

    def format(self, num):
        if num is None:
            return ""
        if num == 0:
            return "ZERO ONLY"
        
        words = self.number_to_words(num)
        return ' '.join(words) + ' ONLY'

    def format_string(self, num_str):
        num = int(num_str)
        return self.format(num)

    def trans_two(self, num_str):
        num = int(num_str)
        return self.number_to_words(num)

    def trans_three(self, num_str):
        num = int(num_str)
        return self.number_to_words(num)

    def parse_more(self, power):
        return self.suffixes[power]

    def number_to_words(self, num):
        if num < 10:
            return [self.ones[num]]
        elif num < 20:
            return [self.teens[num - 10]]
        elif num < 100:
            return [self.tens[num // 10]] + self.number_to_words(num % 10)
        elif num < 1000:
            return [self.ones[num // 100], 'HUNDRED'] + self.number_to_words(num % 100)
        else:
            for i, suffix in enumerate(self.suffixes):
                if num < 1000**(i + 1):
                    return self.number_to_words(num // 1000**i) + [suffix] + self.number_to_words(num % 1000**i)
`