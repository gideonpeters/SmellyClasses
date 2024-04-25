class NLPDataProcessor:
    def __init__(self):
        pass

    @staticmethod
    def construct_stop_word_list():
        return ['a', 'an', 'the']

    @staticmethod
    def remove_stop_words(string_list, stop_word_list):
        words_list = []
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word not in stop_word_list]
            words_list.append(filtered_words)
        return words_list

    @staticmethod
    def process(string_list):
        words_list = []
        for string in string_list:
            words = string.split()
            words_list.append(words)
        return words_list