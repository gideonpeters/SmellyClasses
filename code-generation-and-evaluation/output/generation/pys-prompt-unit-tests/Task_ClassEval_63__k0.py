class NLPDataProcessor2:
    
    @staticmethod
    def process_data(string_list):
        processed_data = []
        for string in string_list:
            processed_string = [word.lower() for word in string.split() if word.isalpha()]
            processed_data.append(processed_string)
        return processed_data

    @staticmethod
    def calculate_word_frequency(words_list):
        word_freq = {}
        for words in words_list:
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        return word_freq

    def process(self, string_list):
        processed_data = self.process_data(string_list)
        word_freq = self.calculate_word_frequency(processed_data)
        return word_freq
