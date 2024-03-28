class LongestWord:
    def __init__(self):
        self.word_list = []

    def add_word(self, word):
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        words = sentence.split()
        longest_word = ''
        for word in words:
            if word.strip('.').strip('!').strip(',').strip('?') in self.word_list:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word.strip('.').strip('!').strip(',').strip('?')
