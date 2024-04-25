class NLPDataProcessor:
    def __init__(self):
        pass

    def construct_stop_word_list(self):
        return ['a', 'an', 'the']

    def remove_stop_words(self, string_list, stop_word_list):
        words_list = []
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word not in stop_word_list]
            words_list.append(filtered_words)
        return words_list

    def process(self, string_list):
        words_list = []
        for string in string_list:
            words = string.split()
            words_list.append(words)
        return words_list
