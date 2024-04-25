class Words2Numbers:
    def __init__(self):
        self.num_dict = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
            'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
            'hundred': 100, 'thousand': 1000, 'million': 1000000
        }

    def text2int(self, text):
        words = text.split()
        total = 0
        current_num = 0
        for word in words:
            if word in self.num_dict:
                current_num = self.num_dict[word]
                if current_num >= 100:
                    total += current_num
                    current_num = 0
                elif current_num >= 10:
                    current_num = max(1, current_num)
            else:
                if word == 'and':
                    continue
                total += current_num
                current_num = 0
        total += current_num
        return str(total)

    def is_valid_input(self, text):
        words = text.split()
        for word in words:
            if word not in self.num_dict and word not in ['and', 'hundred', 'thousand', 'million']:
                return False
        return True
`