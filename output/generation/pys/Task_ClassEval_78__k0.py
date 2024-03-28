class SplitSentence:
    def split_sentences(self, text):
        sentences = []
        sentence = ""
        for char in text:
            sentence += char
            if char in ['.', '?', '!']:
                sentences.append(sentence.strip())
                sentence = ""
        if sentence:
            sentences.append(sentence.strip())
        return sentences

    def count_words(self, text):
        words = text.split()
        return len(words)

    def process_text_file(self, text):
        sentences = self.split_sentences(text)
        return len(sentences)
